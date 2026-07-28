import pandas as pd

#Task 2 — Data Analysis
# Load Dataset
df = pd.read_excel("dataset/Zomato.xlsx")


# 1. Average Restaurant Rating
print("Average Restaurant Rating:")
print(df["Rating"].mean())

# 2. Restaurant with Highest Votes
print("\nRestaurant with Highest Votes:")

highest_votes = df.loc[df["Votes"].idxmax()]

print("Restaurant Name :", highest_votes["RestaurantName"])


# 3. Average Cost for Two
print("\nAverage Cost for Two:")

df["Average_Cost_for_two"] = pd.to_numeric(
    df["Average_Cost_for_two"],
    errors="coerce"
)

print(df["Average_Cost_for_two"].mean())

# 4. Average Rating based on Online Delivery
print("\nAverage Rating by Online Delivery:")

print(
    df.groupby("Has_Online_delivery")["Rating"].mean()
)


# 5. Average Rating based on Table Booking
print("\nAverage Rating by Table Booking:")

print(
    df.groupby("Has_Table_booking")["Rating"].mean()
)

# 6. Top 10 Cities with Highest Number of Restaurants
print("\nTop 10 Cities with Highest Number of Restaurants:")

print(
    df["City"].value_counts().head(10)
)
