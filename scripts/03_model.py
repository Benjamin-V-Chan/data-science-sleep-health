import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load preprocessed data
df = pd.read_csv("data/processed_sleep_data.csv")

# Define features and target
X = df.drop(columns=['Sleep Disorder'])
y = df['Sleep Disorder']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
report = classification_report(y_test, y_pred)

# Save results and model
with open("outputs/classification_report.txt", "w") as f:
    f.write(report)

joblib.dump(model, "outputs/sleep_disorder_model.pkl")
