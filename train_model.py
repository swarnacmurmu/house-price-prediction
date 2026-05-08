import pandas as pd
import numpy as np
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor

# Create model folder if not present
os.makedirs("model", exist_ok=True)

# 1. Load dataset
df = pd.read_csv("data/train.csv")

print("Dataset loaded successfully")
print("Shape:", df.shape)
print(df.head())

# 2. Drop Id column if present
if "Id" in df.columns:
    df = df.drop("Id", axis=1)

# 3. Separate input and output
X = df.drop("SalePrice", axis=1)
y = df["SalePrice"]

# 4. Handle missing values
for col in X.columns:
    if X[col].dtype == "object":
        X[col] = X[col].fillna(X[col].mode()[0])
    else:
        X[col] = X[col].fillna(X[col].median())

# 5. Convert categorical columns to numerical columns
X = pd.get_dummies(X, drop_first=True)

# 6. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 7. Train model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# 8. Predict
y_pred = model.predict(X_test)

# 9. Evaluate
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\nModel Performance:")
print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)

# 10. Save model and columns
joblib.dump(model, "model/house_price_model.pkl")
joblib.dump(X.columns, "model/model_columns.pkl")

print("\nModel saved successfully!")