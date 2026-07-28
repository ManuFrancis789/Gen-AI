import pandas as pd

#Task 1 — Data Understanding & Exploration

#1 Load Dataset
df = pd.read_excel("dataset/Zomato.xlsx")
print(df.columns.tolist())
# Display first 5 rows
print("First 5 Rows:")
print(df.head())

#2a Shape
print("\nShape:")
print(df.shape)

#2b Column Names
print("\nColumns:")
print(df.columns)

#2c Data Types
print("\nData Types:")
print(df.dtypes)

#2d Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

#3 Duplicate Records
print("\nDuplicate Records:")
print(df.duplicated().sum())

#4 Convert Average_Cost_for_two to numeric
df["Average_Cost_for_two"] = pd.to_numeric(
    df["Average_Cost_for_two"],
    errors="coerce"
)

print("\nUpdated Data Type:")
print(df["Average_Cost_for_two"].dtype)

#5 Statistical Summary
print("\nStatistical Summary:")
print(df.describe(include="all"))

#6a Number of Unique Cities
print("\nNumber of Unique Cities:")
print(df["City"].nunique())

#6b City with Highest Number of Restaurants
print("\nCity with Highest Number of Restaurants:")
print(df["City"].value_counts().head(1))

#6c Most Common Cuisine
print("\nMost Common Cuisine:")
print(df["Cuisines"].value_counts().head(1))

