import pandas as pd
import matplotlib.pyplot as plt

# Load and filter
df = pd.read_csv('healthcare_patient_journey.csv')
oncology_seniors = df[(df['age'] > 60) & (df['department'].str.strip() == 'Oncology')]

print(f"Total Oncology patients over 60: {len(oncology_seniors)}")

# Create Chart
plt.figure(figsize=(10, 6))
df['department'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Patient Count by Department')
plt.savefig('department_chart.png') # This saves the image
