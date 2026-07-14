#  Marketing Campaign Data Analysis Project

##  Overview

This project implements an ETL (Extract, Transform, Load) pipeline for a marketing campaign dataset using Python and SQLite. The transformed dataset is prepared for Power BI dashboard creation.

##  Features

- Extracts data from Excel
- Loads data into SQLite database
- Cleans and transforms data
- Performs feature engineering
- Removes missing values and outliers
- Encodes categorical variables
- Exports transformed dataset for visualization
- Maintains execution logs

---

##  Tech Stack

- Python
- Pandas
- NumPy
- SQLite
- SQLAlchemy
- Power BI (In Progress)
- Git & GitHub

---

##  Project Structure

```
Marketing_Campaign_Data_Analyst_Project/
│
├── Database/
│   └── market_data.db
│
├── Dataset/
│   └── marketing_campaign.xlsx
│
├── Logs/
│
├── Updated_Dataset/
│
├── src/
│   ├── data_ingestion.py
│   ├── data_transformation.py
│   └── main.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

##  How to Run

### 1. Clone the repository

```bash
git clone https://github.com/HariprasadBhagat/Marketing_Campaign_Data_Analyst_Project.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Update project paths (if required)

If your local folder structure is different, update the dataset, database, log, and output paths in the source files to match your system.

### 4. Run the project

```bash
python src/main.py
```

`main.py` automatically executes:

- Data Ingestion
- Data Transformation
- Export of transformed dataset

---

##  ETL Workflow

```
Excel Dataset
      │
      ▼
Data Ingestion
      │
      ▼
SQLite Database
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
Outlier Removal
      │
      ▼
Categorical Encoding
      │
      ▼
Transformed Dataset
      │
      ▼
Power BI Dashboard (In Progress)
```

---

##  Project Status

- ✅ Data Ingestion
- ✅ SQLite Integration
- ✅ Data Cleaning
- ✅ Feature Engineering
- ✅ Data Transformation
- ✅ CSV Export
- 🚧 Power BI Dashboard (In Progress)

---

##  Output

The transformed dataset is generated inside:

```
Updated_Dataset/
```

Logs are generated inside:

```
Logs/
```

---

##  Author

**Hariprasad Bhagat**

GitHub: https://github.com/HariprasadBhagat
