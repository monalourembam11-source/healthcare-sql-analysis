# Healthcare Patient Analysis
## Finding: Oncology Patients Over 60

This project uses SQL to filter the `healthcare_patient_journey.csv` dataset.

### The Query Used:
```sql
SELECT count(*)
FROM "healthcare_patient_journey.csv"
WHERE age > 60
AND department = 'Oncology';
