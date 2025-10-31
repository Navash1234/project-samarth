import os
import pandas as pd

# --- Debug info ---
print("Current working directory (cwd):", os.getcwd())
print("Script location:", os.path.dirname(os.path.abspath(__file__)))

# --- Step 1: Load the Excel file ---
file_path = "data/spice_crop_data.xls"   # ✅ Correct relative path
full_path = os.path.join(os.path.dirname(__file__), file_path)

print("Attempting to load:", full_path)

# --- Step 2: Read data ---
try:
    data = pd.read_excel(full_path)
    print("✅ Data loaded successfully!")
    print("First 5 rows:")
    print(data.head())
except Exception as e:
    print("❌ Error loading data:", e)
