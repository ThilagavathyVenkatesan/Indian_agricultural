import pandas as pd

# Load your data
df = pd.read_csv(
    "C:/Users/Modern/Downloads/ICRISAT-District Level Data - ICRISAT-District Level Data.csv",
    low_memory=False
)

# 1. Check if any NULL/NaN values exist in the entire table
print("\n✅ Does the table have any NaN values?")
print(df.isnull().values.any())   # Returns True if any NaN exists

# 2. Count total NaN values in the entire table
print("\n📊 Total NaN values in the table:")
print(df.isnull().sum().sum())

# 3. Count NaN values column-wise
print("\n🧾 NaN values per column:")
print(df.isnull().sum())

# 4. Optional: View rows with *any* NaN in them
print("\n🔍 Sample rows with any NaN values:")
print(df[df.isnull().any(axis=1)].head())



