import pandas as pd
from pathlib import Path

# Define paths
base_dir = Path(__file__).resolve().parent
crop_data_path = base_dir / "clean_data" / "spice_crop_cleaned.csv"
rain_data_path = base_dir / "data" / "rainfall_data.csv"
output_path = base_dir / "clean_data" / "merged_crop_rainfall.csv"

# Load datasets
print("🔹 Loading datasets...")
crop_df = pd.read_csv(crop_data_path)
rain_df = pd.read_csv(rain_data_path)

# Merge on common columns (state + year)
print("🔹 Merging on 'state' and 'year'...")
merged_df = pd.merge(crop_df, rain_df, on=["state", "year"], how="left")

# Save merged output
merged_df.to_csv(output_path, index=False)
print(f"✅ Merged dataset saved to: {output_path}")

# Show sample output
print("\n📊 Preview of merged data:")
print(merged_df.head())