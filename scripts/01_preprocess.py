import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load dataset
df = pd.read_csv("data/Sleep_health_and_lifestyle_dataset.csv")

# Handle missing values
df.fillna("None", inplace=True)

# Split Blood Pressure into two separate columns
df[['Systolic_BP', 'Diastolic_BP']] = df['Blood Pressure'].str.split('/', expand=True).astype(float)
df.drop(columns=['Blood Pressure'], inplace=True)

# Encode categorical variables
encoder = LabelEncoder()
for col in ['Gender', 'Occupation', 'BMI Category', 'Sleep Disorder']:
    df[col] = encoder.fit_transform(df[col])

# Normalize numerical columns
scaler = StandardScaler()
num_cols = ['Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 
            'Stress Level', 'Heart Rate', 'Daily Steps', 'Systolic_BP', 'Diastolic_BP']
df[num_cols] = scaler.fit_transform(df[num_cols])

# Save processed data
df.to_csv("data/processed_sleep_data.csv", index=False)
