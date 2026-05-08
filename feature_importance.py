import joblib
import pandas as pd
import matplotlib.pyplot as plt
import os

os.makedirs("model", exist_ok=True)

# Load trained model and column names
model = joblib.load("model/house_price_model.pkl")
columns = joblib.load("model/model_columns.pkl")

# Get feature importance values from model
importance = model.feature_importances_

# Create dataframe
feature_df = pd.DataFrame({
    "Feature": columns,
    "Importance": importance
})

# Sort and take top 15 features
feature_df = feature_df.sort_values(
    by="Importance",
    ascending=False
).head(15)

# Plot graph
plt.figure(figsize=(10, 6))
plt.barh(feature_df["Feature"], feature_df["Importance"])

plt.xlabel("Importance Score")
plt.ylabel("Feature")
plt.title("Top 15 Important Features")

plt.gca().invert_yaxis()
plt.tight_layout()

# Save graph
plt.savefig("model/feature_importance.png")

print("Feature importance graph saved successfully!")