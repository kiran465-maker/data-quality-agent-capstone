📄 **README.md**


# 📘 **Data Quality Agent Pipeline – Capstone Project**

## 🚀 Overview

The **Data Quality Agent Pipeline** is an automated system designed to ensure that any dataset—raw, messy, or incomplete—can be processed and transformed into a *clean, validated, and analysis-ready* format.

This project uses a modular **Agent-based architecture**, where each agent is responsible for a specific task:

* 🟦 **Ingestion Agent** – loads the raw dataset
* 🟩 **Quality Check Agent** – identifies missing values, invalid types, and structural issues
* 🟨 **AutoFix Agent** – applies automated cleaning & fixes
* 🟧 **Validation Agent** – generates a validation report
* 🟪 **Reporting Agent** – outputs pipeline results

The pipeline is built in Python and can handle **any CSV dataset**, making it ideal for real-world data work, ETL processes, production workflows, and Kaggle competitions.

---

## 🧠 Key Features

✔ Modular agent-based system
✔ Fully automated end-to-end pipeline
✔ Ingestion, cleaning, validation, and reporting
✔ Works with any CSV file
✔ Generates output files automatically
✔ Easy to integrate into data engineering workflows
✔ Beginner-friendly & production-ready structure

---

## 📂 Project Structure

```
data-quality-agent-capstone/
│
├── app.py
├── README.md
│
├── agents/
│   ├── ingestion_agent.py
│   ├── quality_check_agent.py
│   ├── autofix_agent.py
│   ├── validation_agent.py
│   ├── reporting_agent.py
│
├── data/
│   ├── input/
│   │   └── raw.csv
│   └── output/
│       ├── cleaned.csv
│       ├── validation_report.json
│       └── summary.txt
│
├── tests/
│   └── test_agents.py
│
└── tools/
    └── helpers.py
```

---

## 🛠 Requirements

### 🔧 Software

Install these on Windows:

* Python 3.10+
* pip
* Git
* VS Code (optional but recommended)

### 📦 Python Libraries

Install using:

```
pip install -r requirements.txt
```

(If you don’t have the file, your project only needs pandas.)

---

## ▶️ How to Run the Pipeline

### **Step 1 – Place your dataset**

Put a CSV file into:

```
data/input/raw.csv
```

Example:

```
data/input/raw.csv
```

### **Step 2 – Run the app**

Open CMD or VS Code terminal:

```
python app.py
```

### ✔ You should see:

```
=== DATA QUALITY AGENT PIPELINE STARTED ===

[STEP 1] Ingestion completed.
[STEP 2] Quality Check completed.
[STEP 3] Autofix completed.
[STEP 4] Validation completed.

=== PIPELINE FINISHED SUCCESSFULLY ===
```

### **Step 3 – Check the outputs**

After running, check:

```
data/output/cleaned.csv
data/output/validation_report.json
data/output/summary.txt
```

## 🧪 Tests

To run tests:

```
python -m pytest tests/
```

## 🧩 Agents Explained

### 1️⃣ Ingestion Agent

Loads the input CSV.

### 2️⃣ Quality Check Agent

Runs basic checks:

* Null counts
* Datatype info
* Summary statistics

### 3️⃣ AutoFix Agent

Applies simple fixes:

* Fills missing values
* Saves cleaned file

### 4️⃣ Validation Agent

Creates a structured validation report:

```
{
  "rows": 100,
  "columns": ["A","B","C"],
  "missing_values": { ... }
}
```

### 5️⃣ Reporting Agent

Produces a simple text summary.

## Why This Project Stands Out

✔ Real-world ETL pipeline
✔ Fully automated
✔ Agent-based clean architecture
✔ Works on any dataset
✔ Beginner-friendly but industry-oriented
✔ Modular for future extension


## Author

**kiran**
(Data Engineering Enthusiast)
