import pandas as pd

# Load Dataset
df = pd.read_excel("dataset/Zomato.xlsx")


# 1. City with Highest Restaurant Presence
top_city = df["City"].value_counts().idxmax()

print("1. City with Highest Restaurant Presence:")
print(top_city)

# 2. Most Popular Cuisine
top_cuisine = df["Cuisines"].value_counts().idxmax()

print("\n2. Most Popular Cuisine:")
print(top_cuisine)

# 3. Do Restaurants with Online Delivery Have Higher Ratings?
online_rating = df.groupby("Has_Online_delivery")["Rating"].mean()

print("\n3. Average Rating by Online Delivery:")
print(online_rating)

if online_rating["Yes"] > online_rating["No"]:
    print("\nConclusion:")
    print("Restaurants with Online Delivery generally have higher ratings.")
elif online_rating["Yes"] < online_rating["No"]:
    print("\nConclusion:")
    print("Restaurants without Online Delivery generally have higher ratings.")
else:
    print("\nConclusion:")
    print("Both groups have similar average ratings.")

# 4. Do Restaurants with Table Booking Have Better Ratings?
booking_rating = df.groupby("Has_Table_booking")["Rating"].mean()

print("\n4. Average Rating by Table Booking:")
print(booking_rating)

if booking_rating["Yes"] > booking_rating["No"]:
    print("\nConclusion:")
    print("Restaurants offering Table Booking generally receive better ratings.")
elif booking_rating["Yes"] < booking_rating["No"]:
    print("\nConclusion:")
    print("Restaurants without Table Booking generally receive better ratings.")
else:
    print("\nConclusion:")
    print("Both groups have similar average ratings.")

# 5. Final Learning
print("\n5. What Did I Learn From This Dataset?")

print("""
- Explored a real-world restaurant dataset using Pandas.
- Performed data cleaning and checked for missing values and duplicates.
- Analyzed restaurant ratings, costs, votes, cities, and cuisines.
- Created visualizations using Matplotlib.
- Drew business insights based on restaurant data.
""")
