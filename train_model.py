import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("dataset/train.csv")

# Features
features = [
    "OverallQual",
    "GrLivArea",
    "GarageCars",
    "GarageArea",
    "TotalBsmtSF",
    "FullBath",
    "BedroomAbvGr",
    "YearBuilt"
]

X = df[features]
y = df["SalePrice"]

# Fill missing values
X = X.fillna(X.mean())

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()

model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

score = r2_score(y_test, predictions)

print(f"Model Accuracy (R² Score): {score:.4f}")

# Save model
joblib.dump(model, "house_model.pkl")

print("Model saved successfully!")