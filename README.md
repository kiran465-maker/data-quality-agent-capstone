# **Data Quality Agent – Capstone Project**

This project implements a modular, multi-agent system designed to automate end-to-end data quality processing. Each agent is responsible for a specific stage in the workflow, ensuring that raw data is ingested, assessed, cleaned, validated, and summarized in a systematic and reliable manner.

The system is suitable for data engineering, ETL pipelines, and automated data quality assessment workflows.

---

## **1. Project Overview**

Modern data workflows rely heavily on clean and reliable datasets. This project provides an **agent-based pipeline** where each agent performs an independent and well-defined task. Together, the agents transform an input CSV file into a cleaned, validated dataset along with detailed reports.

The pipeline processes:

* Raw data ingestion
* Quality issue detection
* Automatic data cleaning
* Rule-based validation
* Report generation

The project is built to be **extensible**, **easy to maintain**, and **clear in responsibility separation**.

---

## **2. Directory Structure**

```
data-quality-agent-capstone/
│
├── app.py                         # Main orchestrator that runs the pipeline
├── README.md                      # Documentation
│
├── agents/
│   ├── ingestion_agent.py         # Reads and loads raw data
│   ├── quality_check_agent.py     # Identifies data quality issues
│   ├── autofix_agent.py           # Automatically fixes identified issues
│   ├── validation_agent.py        # Validates data against defined rules
│   ├── reporting_agent.py         # Generates final reports and summaries
│
├── data/
│   ├── input/
│   │   └── raw.csv                # User-provided raw dataset
│   └── output/
│       ├── cleaned.csv            # Cleaned output file
│       ├── validation_report.json # JSON report on validation results
│       └── summary.txt            # Summary of checks and fixes applied
│
├── tools/
│   └── helpers.py                 # Shared helper functions
│
└── tests/
    └── test_agents.py             # Unit tests for individual agents
```

---

## **3. Pipeline Workflow**

### **3.1 Ingestion Agent**

* Loads `raw.csv` from the input directory
* Converts the file into a structured format (Pandas DataFrame)
* Performs initial format checks
* Passes data to the next stage

### **3.2 Quality Check Agent**

* Detects data anomalies including:

  * Missing values
  * Duplicate records
  * Type inconsistencies
  * Unexpected values

* Produces an internal report of identified issues

### **3.3 AutoFix Agent**

* Applies automated corrections where possible:

  * Handling missing values
  * Removing duplicates
  * Formatting corrections
  * Standardizing string and numeric formats

* Outputs a cleaned dataset as `cleaned.csv`

### **3.4 Validation Agent**

* Validates cleaned data against rules such as:

  * Expected schema
  * Required columns
  * Allowed ranges
  * Business constraints

* Outputs detailed validation information in `validation_report.json`

### **3.5 Reporting Agent**

* Summarizes the full workflow including:

  * Quality issues detected
  * Fixes applied
  * Validation outcomes

* Generates a final `summary.txt` report in human-readable format

---

## **4. How to Run**

### **Step 1: Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Step 2: Insert Your Input File**

Place your raw dataset in:

```
data/input/raw.csv
```

### **Step 3: Execute the Pipeline**

```bash
python app.py
```

### **Step 4: Review Output Files**

Generated files will appear in:

```
data/output/cleaned.csv
data/output/validation_report.json
data/output/summary.txt
```

---

## **5. Testing**

Unit tests are included for verifying agent behavior.

Run tests using:

```bash
pytest tests/
```

---

## **6. Key Features**

* Modular and maintainable architecture
* Automated data quality assessment
* Automated data cleaning
* Rule-based validation
* Clear and structured output reports
* Simple to integrate into larger ETL workflows

---

## **7. Future Enhancements**

Possible improvements include:

* Machine learning-driven anomaly detection
* Support for multiple input formats
* Enhanced reporting with visualizations
* CLI-based pipeline dashboard
* Cloud deployment with serverless execution

---

## **8. Summary**

This project demonstrates a clean and practical approach to data quality management using an agent-based architecture. It aims to balance clarity, modularity, and effectiveness, offering a useful foundation for real-world data engineering scenarios.

---
