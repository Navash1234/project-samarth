import pandas as pd

# Load your merged dataset
data_path = "clean_data/merged_crop_rainfall.csv"
df = pd.read_csv(data_path)

print("✅ Data loaded. You can now ask questions about rainfall, crop production, or correlation.")
print("Type 'exit' to quit.\n")

while True:
    question = input("Ask your question: ").lower()

    if question in ["exit", "quit"]:
        print("Goodbye! 👋")
        break

    # ---- Question 1: Highest / Lowest production ----
    elif "highest" in question and "production" in question:
        top = df.loc[df["production"].idxmax()]
        print(f"🏆 Highest production: {top['district_name']} with {top['production']:.2f} tonnes.")
        print(f"Rainfall: {top['avg_annual_rainfall_mm']} mm — Source: data.gov.in\n")

    elif "lowest" in question and "production" in question:
        low = df.loc[df["production"].idxmin()]
        print(f"🔻 Lowest production: {low['district_name']} with {low['production']:.2f} tonnes.")
        print(f"Rainfall: {low['avg_annual_rainfall_mm']} mm — Source: data.gov.in\n")

    # ---- Question 2: Average rainfall ----
    elif "average" in question and "rainfall" in question:
        avg_rain = df["avg_annual_rainfall_mm"].mean()
        print(f"🌧 Average annual rainfall: {avg_rain:.2f} mm — Source: data.gov.in\n")

    # ---- Question 3: Correlation ----
    elif "correlation" in question or "relationship" in question:
        corr = df["production"].corr(df["avg_annual_rainfall_mm"])
        if pd.isna(corr):
            print("📊 Rainfall values are constant, so correlation cannot be computed.")
            print("Try using a dataset with year-wise or district-wise rainfall variation.\n")
        else:
            print(f"📈 Correlation between rainfall and production: {corr:.2f}")
            if corr > 0:
                print("Interpretation: As rainfall increases, production tends to increase.\n")
            elif corr < 0:
                print("Interpretation: Higher rainfall seems to reduce production.\n")
            else:
                print("Interpretation: No clear correlation.\n")