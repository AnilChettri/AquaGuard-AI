# app/train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load data
df = pd.read_csv('model/water_quality_data.csv')

# Prepare data for training
X = df[['pH', 'Temperature', 'Turbidity']]
y = df['Label'].apply(lambda x: 1 if x == 'Contaminated' else 0)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Test the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the model to a file
joblib.dump(model, 'model/water_quality_model.pkl')
print("Model saved as water_quality_model.pkl")
