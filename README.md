# Data Cleaning & Preprocessing Examples

This repository contains **sample Python scripts** for data cleaning and preprocessing, designed to demonstrate core data engineering skills.  
The scripts can be used as standalone utilities or integrated into larger **ETL (Extract, Transform, Load)** pipelines.

---

##  Features
-  Remove duplicate rows  
-  Handle missing values (drop or impute)  
-  Rename and standardize column names  
-  Convert between CSV, Excel, and JSON formats  
-  Save cleaned data for analytics or machine learning  

---

##  Project Structure

data-cleaning/

├── clean_csv.py # Main script for cleaning CSV files

├── input.csv # Example input file (sample data)

└── output_clean.csv # Example cleaned output

---

##  How to Run
1. Install dependencies (requires Python 3.8+):
   ```bash
   pip install pandas

Place your raw CSV file as input.csv in the same directory.

2. Run the script:
   ```bash
   python clean_csv.py

The cleaned dataset will be saved as:
output_clean.csv

### Example Use Case

Imagine you have a raw dataset full of duplicate records and missing values:

Input (input.csv):
id,name,age
1,Ali,30
2,Reza,
2,Reza,
3,Sara,25

id,name,age
1,Ali,30
2,Reza,NaN
3,Sara,25


### Author:

Ali Zamanpour

Freelance Data Engineer & AI Specialist

Expertise: Python, SQL, ETL, Machine Learning

###License:

This project is licensed under the MIT License – feel free to use and adapt it for your own projects.
