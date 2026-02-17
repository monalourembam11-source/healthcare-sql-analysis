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

💡 Executive Summary: What the Data Tells Us
Beyond the numbers, this analysis provides critical insights into the patient population and hospital resource allocation:

Significant Senior Demographic: The 221 oncology patients over age 60 represent 22.1% of the total patient load. This highlights a clear need for specialized geriatric-oncology resources and age-friendly facility navigation.

Strategic Resource Allocation: With nearly a quarter of the population being seniors in a high-intensity department, the data supports prioritizing mobility assistance, integrated pharmacy consultations, and social work support for long-term care planning.

Cross-Platform Reliability: By achieving identical results (221) across SQL, Python, and R, we have established a "Gold Standard" dataset. This high level of data integrity ensures that any subsequent medical or financial decisions are based on verified, accurate information.

---
### 1. SQL (Extraction)
Used for the primary data query.
sql
SELECT count(*)
FROM "healthcare_patient_journey.csv"
WHERE age > 60 AND department = 'Oncology';


