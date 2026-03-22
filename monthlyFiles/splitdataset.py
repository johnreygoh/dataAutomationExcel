import pandas as pd
import os

# Create directory for the capstone
output_dir = '.'
os.makedirs(output_dir, exist_ok=True)

print("Reading main sales file...")
df = pd.read_csv('Sales_Transactions.csv')
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

print("Splitting into 12 monthly files...")
# Filter for just the year 2025 to get exactly 12 months
df_2025 = df[df['OrderDate'].dt.year == 2025]

for month in range(1, 13):
    month_data = df_2025[df_2025['OrderDate'].dt.month == month]
    if not month_data.empty:
        filename = f"{output_dir}\\Sales_2025_{month:02d}.csv"
        month_data.to_csv(filename, index=False)
        print(f"Created: {filename}")

print("All 12 monthly files generated successfully!")