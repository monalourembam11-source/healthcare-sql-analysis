# 🏥 Healthcare Patient Journey Analysis

![SQL](https://img.shields.io/badge/SQL-00758F?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

## 🎯 Project Objective
The goal of this analysis was to identify high-priority patient demographics—specifically **Oncology patients aged 60 and older**—within a dataset of 3,000 patient journeys.

### 📊 The Finding
Through a "Triple-Verification" workflow, I confirmed a final count of **221 patients** meeting these criteria.

---

## 🛠️ Multi-Tool Implementation
To ensure 100% data integrity, I processed the data using three different environments such as SQL, Python and R. Each script achieves the same result:

### 1. SQL (Extraction)
Used for the primary data query.
```sql
SELECT count(*)
FROM "healthcare_patient_journey.csv"
WHERE age > 60 AND department = 'Oncology';
