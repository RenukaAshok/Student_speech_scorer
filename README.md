# 🎤 Student Introduction Rubric Scorer
A rule-based Streamlit web application that evaluates a student's introduction transcript based on a structured rubric.  
Built for the **Nirmaan AI Intern Case Study**.

---

## 📌 Project Overview

This tool evaluates a student's *spoken introduction* (converted into text) using a clean, structured rubric.  
The user pastes the transcript, and the app generates:

- ✔ Per-criterion scores  
- ✔ Keyword coverage  
- ✔ Length suitability  
- ✔ Constructive feedback  
- ✔ Weighted overall communication score  

This scoring system helps assess clarity, completeness, and communication skills.

---

## 🚀 Features

### **1. Four-Criterion Rubric**
The transcript is evaluated on four major components:

1. **Basic Self-Introduction**  
2. **Family & Background**  
3. **Interests & Hobbies**  
4. **Academic Interests & Future Goals**

Each includes:
- Keywords  
- Weightage  
- Expected word range  

---

### **2. Keyword + Length Based Evaluation**
The app calculates:
- Presence of keywords  
- Whether the transcript fits the expected length  
- Combined rule-based score for each criterion  

---

### **3. Clean & Professional UI**
- Simple white interface  
- Dark-blue sidebar  
- Rubric summary table  
- Developer credit shown as **“Developed by Renuka A”**  

---

### **4. No Excel Required in App**
Although the case study included an Excel rubric,  
the rubric is **implemented directly inside the app**,  
making the tool lightweight and deployment-ready.

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- NumPy  
- Pandas  

---

## 📦 Installation (Using Windows Command Prompt)

You can run this project directly through the **Windows Command Prompt** by following these steps:

### 1️⃣ Create your project folder
Create a folder on your system nirmaan_intro_scorer
Add files

Place these files inside the folder:
- `app.py`
- `requirements.txt`
- `README.md`

---

### 2️⃣ Open Command Prompt

Press **Win + R**, type `cmd`, and press **Enter**.

---

### 3️⃣ Navigate to your project folder

```bash
cd C:\Users\sss\Desktop\nirmaan_intro_scorer

Install the dependencies
pip install -r requirements.txt

Run the Application
streamlit run app.py








