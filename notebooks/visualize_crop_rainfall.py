import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Define path
base_dir = Path(__file__).resolve().parent.parent
merged_data_path = base_dir / "clean_data" / "merged_crop_rainfall.csv"

# Load dataset
df = pd.read_csv(merged_data_path)
print("✅ Data loaded for visualization")
print(df.head())

# --- Example 1: Correlation between rainfall and production ---
plt.figure(figsize=(8,6))
plt.scatter(df["avg_annual_rainfall_mm"], df["production"], color="teal")
plt.title("Rainfall vs Production (2021)")
plt.xlabel("Average Annual Rainfall (mm)")
plt.ylabel("Spice Production (tonnes)")
plt.grid(True)
plt.tight_layout()
plt.show()

# --- Example 2: Bar chart of top 10 districts by production ---
top10 = df.sort_values("production", ascending=False).head(10)
plt.figure(figsize=(10,6))
plt.barh(top10["district_name"], top10["production"], color="orange")
plt.title("Top 10 Districts by Spice Production (2021)")
plt.xlabel("Production (tonnes)")
plt.ylabel("District")
plt.tight_layout()
plt.show()