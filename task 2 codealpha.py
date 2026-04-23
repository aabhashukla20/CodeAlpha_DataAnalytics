import pandas as pd
df = pd.read_csv("amazon_reviews.csv")
print(df.head())
# Load dataset
df = pd.read_csv("amazon_reviews.csv")

# Basic structure
print("Shape:", df.shape)
print(df.head())

# Data types
print(df.info())

# Missing values
print("Missing values:\n", df.isnull().sum())

# Drop missing rows
df = df.dropna()

# Basic statistics
print(df.describe())

# Unique values
print("Unique Ratings:", df["rating"].unique())

# Insights
print("Average Rating:", df["rating"].mean())
print("Max Rating:", df["rating"].max())
print("Min Rating:", df["rating"].min())