import re
import numpy as np
import pandas as pd
import streamlit as st

# ---------- TEXT UTILITIES ----------

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        text = str(text)
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text

def word_count(text: str) -> int:
    return len(text.split())

def keyword_coverage(transcript: str, keywords: str):
    if not isinstance(keywords, str) or not keywords.strip():
        return 1.0, [], []

    kws = [k.strip().lower() for k in keywords.split(",") if k.strip()]
    text_lower = transcript.lower()

    found = []
    missing = []
    for k in kws:
        if k in text_lower:
            found.append(k)
        else:
            missing.append(k)

    if len(kws) == 0:
        return 1.0, [], []

    score = len(found) / len(kws)
    return score, found, missing

def length_score(total_words: int, min_words, max_words):
    if (min_words is None or pd.isna(min_words)) and (max_words is None or pd.isna(max_words)):
        return 1.0

    if min_words is None or pd.isna(min_words):
        min_words = 0
    if max_words is None or pd.isna(max_words):
        max_words = 10**9

    if min_words <= total_words <= max_words:
        return 1.0
    elif (0.8 * min_words) <= total_words <= (1.2 * max_words):
        return 0.5
    else:
        return 0.0

# ---------- SCORING ----------

def score_criterion(row, transcript: str, total_words: int):
    name = row.get("criterion_name", "")
    desc = row.get("description", "")
    keywords = row.get("keywords", "")
    weight = row.get("weight", 1.0)
    min_w = row.get("min_words", None)
    max_w = row.get("max_words", None)

    kw_score, found_kws, missing_kws = keyword_coverage(transcript, keywords)
    len_score = length_score(total_words, min_w, max_w)

    combined = 0.7 * kw_score + 0.3 * len_score
    crit_score = combined * 100

    if len_score == 1:
        length_fb = "Length is within the recommended range."
    elif len_score == 0.5:
        length_fb = "The introduction length is slightly off the suggested range."
    else:
        length_fb = "Length is far from recommended; consider adjusting."

    return {
        "criterion_name": name,
        "weight": weight,
        "score": crit_score,
        "keyword_score": kw_score,
        "length_score": len_score,
        "keywords_found": found_kws,
        "keywords_missing": missing_kws,
        "length_feedback": length_fb,
        "description": desc,
    }

def aggregate_overall(results):
    if not results:
        return 0
    total_weight = sum(r["weight"] for r in results)
    weighted_sum = sum(r["score"] * r["weight"] for r in results)
    return weighted_sum / total_weight if total_weight else 0

# ---------- RUBRIC ----------

def get_default_rubric():
    data = [
        {"criterion_name": "Basic self-introduction",
         "description": "Student clearly states name, class, and school.",
         "keywords": "name, class, school",
         "weight": 0.25, "min_words": 30, "max_words": 200},

        {"criterion_name": "Family & background",
         "description": "Student mentions family members or personal background.",
         "keywords": "family, mother, father, special",
         "weight": 0.25, "min_words": 20, "max_words": 200},

        {"criterion_name": "Interests & hobbies",
         "description": "Student talks about hobbies or what they enjoy doing.",
         "keywords": "hobby, enjoy, like, cricket, reading, music",
         "weight": 0.20, "min_words": 20, "max_words": 200},

        {"criterion_name": "Academic interest & goals",
         "description": "Student talks about favourite subject or future goals.",
         "keywords": "favorite subject, favourite subject, science, maths, future, goal, explore",
         "weight": 0.30, "min_words": 20, "max_words": 200},
    ]
    return pd.DataFrame(data)

# ---------- STYLING (NO BACKGROUND IMAGE) ----------

def add_styles():
    st.markdown("""
    <style>
        body { color: #000; }
        .content-card {
            background-color: #ffffff;
            padding: 1.3rem 1.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 14px rgba(0,0,0,0.10);
        }
        [data-testid="stSidebar"] {
            background-color: #0b3b70 !important;
        }
        [data-testid="stSidebar"] * {
            color: white !important;
        }
        .rubric-header {
            background:#000;
            padding:6px;
            color:#fff;
            text-align:center;
            border-radius:6px;
            font-weight:600;
        }
        .rubric-table {
            margin-top:8px;
            background:#133b7a;
            color:white;
            padding:8px;
            border-radius:8px;
            font-size:0.85rem;
        }
    </style>
    """, unsafe_allow_html=True)

# ---------- STREAMLIT APP ----------

def main():
    st.set_page_config(page_title="Student Introduction Scorer", layout="wide")
    add_styles()

    rubric_df = get_default_rubric()

    # ------ Sidebar developer credit ------
    st.sidebar.markdown(
        "<p style='color:white; font-weight:600; font-size:16px; margin-bottom:18px;'>Developed by Renuka A</p>",
        unsafe_allow_html=True
    )

    # Sidebar rubric box
    st.sidebar.markdown("<div class='rubric-header'>Rubric Summary</div>", unsafe_allow_html=True)
    st.sidebar.markdown("<div class='rubric-table'>", unsafe_allow_html=True)
    st.sidebar.table(rubric_df[["criterion_name", "weight", "min_words", "max_words"]])
    st.sidebar.markdown("</div>", unsafe_allow_html=True)

    # Main card container
    st.markdown("<div class='content-card'>", unsafe_allow_html=True)
    st.title("🎤 Student Introduction – Rubric Scorer")

    st.write("Enter the student's introduction below. The system evaluates clarity, completeness, and structure based on the rubric.")

    transcript = st.text_area(
        "Transcript Input",
        value="",
        height=220,
        placeholder="Paste or type the student's introduction here..."
    )

    if st.button("🚀 Score my intro"):
        text = clean_text(transcript)
        total = word_count(text)

        if total == 0:
            st.error("Please enter some text before scoring.")
        else:
            st.subheader("📏 Basic Stats")
            st.write(f"**Total Words:** {total}")

            results = [score_criterion(row, text, total) for _, row in rubric_df.iterrows()]
            overall = aggregate_overall(results)

            st.subheader("🎯 Overall Score")
            st.metric("Communication Score", f"{overall:.1f}")

            st.subheader("📊 Detailed Feedback")
            for r in results:
                with st.expander(f"{r['criterion_name']} – {r['score']:.1f}/100"):
                    st.write(f"**Description:** {r['description']}")
                    st.write(f"**Keyword Score:** {r['keyword_score']:.2f}")
                    st.write(f"**Length Score:** {r['length_score']:.2f}")
                    st.write(f"**Length Feedback:** {r['length_feedback']}")
                    st.write(f"**Found Keywords:** {', '.join(r['keywords_found']) or 'None'}")
                    st.write(f"**Missing Keywords:** {', '.join(r['keywords_missing']) or 'None'}")

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
