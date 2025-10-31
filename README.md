
## 🛰 Project Samarth — Intelligent Q&A System on Government Data

### 📘 Overview

*Project Samarth* is a data-driven prototype that connects datasets from *data.gov.in* and *IMD (India Meteorological Department)* to answer questions about India’s agricultural production and climate patterns.
The system demonstrates how government open data can be integrated, cleaned, and queried intelligently using Python.

---

### 🎯 Objective

Government datasets are often released in disconnected formats across different ministries.
This project aims to:

* Combine *agricultural* and *climate* data into a unified database.
* Enable users to ask *natural language questions* (like rainfall vs crop production).
* Provide *accurate, source-traceable answers* with real data citations.

---

### 🧩 Project Structure


project_samarth/
│
├── data/                     # Raw data (spice_crop_data.xls)
├── clean_data/               # Cleaned datasets
├── notebooks/                # Jupyter notebooks (optional analysis)
├── visuals/                  # Graphs or plots
├── reports/                  # Output summaries or documentation
├── etl_load_crop_data.py     # ETL script (load & clean raw data)
├── merge_rainfall_crop.py    # Merges crop data with rainfall info
├── qa_engine.py              # Q&A system prototype
└── README.md


---

### ⚙ How to Run

1. *Install dependencies*

   bash
   pip install pandas numpy openpyxl xlrd
   

2. *Run ETL (data loading & cleaning)*

   bash
   python etl_load_crop_data.py
   

3. *Merge rainfall and crop data*

   bash
   python merge_rainfall_crop.py
   

4. *Start Q&A engine*

   bash
   python qa_engine.py
   

   You can then type questions like:

   * What is the total production in Karnataka?
   * Compare rainfall and production.
   * Which district has the highest spice production?

---

### 🧠 Example Output


Ask your question: Compare rainfall and production
📈 Correlation between rainfall and production: 0.82
Interpretation: Higher rainfall is associated with higher production.


---

### 📊 Tools & Technologies

* *Python 3.12*
* *Pandas, **NumPy*
* *OpenPyXL, **xlrd*
* *Data Source:* [data.gov.in](https://data.gov.in)

---

### 🪄 Key Features

✅ Data Cleaning & Integration
✅ Query-based Answers (Text Input)
✅ Real Dataset Usage
✅ Expandable Architecture

---

### 🔒 Core Values

* *Accuracy* — All outputs are computed from real data.
* *Traceability* — Data sources clearly cited.
* *Data Sovereignty* — Works fully offline and locally.

---

### 🎥 Demo

You can view a 2-minute Loom walkthrough video showing:

* Dataset loading
* Q&A system running live
* Explanation of system design

(Add your Loom link here after recording)
➡ *Demo Video:* [https://www.loom.com/share/ade8aa5d64ed45f1a798d07b6586cdb3](#)

---

### 👩‍💻 Author

*Aysha K*
Project Samarth — Intelligent Q&A System Prototype

---

Would you like me to make the same README.md in *Markdown format (ready to upload)* so you can directly copy it into your VS Code folder?
