# 🏥 Healthcare Patient Journey: SQL Analysis

### 📋 Project Overview
This project demonstrates the use of SQL to extract meaningful insights from healthcare data. I analyzed a patient journey dataset to identify specific high-risk demographics that require specialized medical attention.

### 📊 Key Finding
After querying the dataset, I identified the specific volume of senior patients in the Oncology department.

* **Target Group:** Patients aged 61 and older.
* **Department:** Oncology.
* **Final Count:** **221 Patients**

### 💻 The Query
I used the following SQL query to ensure accuracy, account for case sensitivity, and filter the data correctly:

```sql
SELECT count(*)
FROM "healthcare_patient_journey.csv"
WHERE age > 60
AND department = 'Oncology';
![Department Analysis Chart](department_chart.png)
