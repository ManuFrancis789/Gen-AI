import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_excel("dataset/Zomato_75_Restaurants.xlsx")


# 1. Bar Chart -Top 10 Cities with Highest Number of Restaurants
top_cities = df["City"].value_counts().head(10)

plt.figure(figsize=(10,5))
top_cities.plot(kind="bar")
plt.title("Top 10 Cities with Highest Number of Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Histogram - Distribution of Restaurant Ratings
plt.hist(df["Rating"], bins=10)
plt.title("Distribution of Restaurant Ratings")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 3. Bar Chart - Restaurants Offering Online Delivery
online_delivery = df["Has_Online_delivery"].value_counts()

plt.figure(figsize=(6,5))
online_delivery.plot(kind="bar")
plt.title("Restaurants Offering Online Delivery")
plt.xlabel("Online Delivery")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 4. Bar Chart - Top 10 Most Common Cuisines
top_cuisines = df["Cuisines"].value_counts().head(10)

plt.figure(figsize=(12,5))
top_cuisines.plot(kind="bar")
plt.title("Top 10 Most Common Cuisines")
plt.xlabel("Cuisine")
plt.ylabel("Number of Restaurants")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# 5. Line Chart - Average Rating by Price Range
rating_price = df.groupby("Price_range")["Rating"].mean()

plt.figure(figsize=(8,5))
plt.plot(rating_price.index, rating_price.values, marker='o')
plt.title("Average Restaurant Rating by Price Range")
plt.xlabel("Price Range")
plt.ylabel("Average Rating")
plt.grid(True)
plt.tight_layout()
plt.show()
