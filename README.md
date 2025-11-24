# 🎤 Student Introduction Rubric Scorer
A rule-based Streamlit web application that evaluates a student's introduction transcript based on a structured rubric.  
Built for the **Nirmaan AI Intern Case Study**.

---

## 📌 Project Overview

This tool evaluates a student's *spoken introduction* (converted into text) using a clear, structured rubric.  
The user pastes the transcript, and the app calculates:

- ✔ Per-criterion scores  
- ✔ Keyword coverage  
- ✔ Length suitability  
- ✔ Weighted overall score  
- ✔ Constructive feedback  

The scoring focuses on clarity, completeness, and communication structure.

---

## 🚀 Features

### **1. Four-Criterion Rubric**
The transcript is evaluated on:

1. **Basic Self-Introduction**  
2. **Family & Background**  
3. **Interests & Hobbies**  
4. **Academic Interests & Future Goals**

Each includes:
- Keywords  
- Weightage  
- Recommended word range  

---

### **2. Keyword + Length Evaluation**
The app checks:
- Presence of essential keywords  
- Whether the transcript fits the expected length  
- Combined rule-based score for each criterion  

---

### **3. Clean & Professional UI**
- Simple white interface  
- Dark-blue sidebar  
- Rubric shown in a clean table  
- Developer credit shown as **“Developed by Renuka A”**  

---

### **4. No Excel Required**
Although the case study included an Excel rubric,  
the rubric is **implemented directly in the app**,  
making the system fast, lightweight, and deployment-ready.

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Pandas  
- NumPy  

---

## 📦 Installation

Install all dependencies:

```bash
pip install -r requirements.txt

