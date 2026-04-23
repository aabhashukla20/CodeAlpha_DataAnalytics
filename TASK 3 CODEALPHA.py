import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

data = {
    "review": ["Good", "Bad", "Average", "Excellent", "Poor"],
    "rating": [5, 1, 3, 5, 2]
}

df = pd.DataFrame(data)
df.to_csv("amazon_reviews.csv", index=False)

print("File fixed!")

# Check if file exists
file_path = "amazon_reviews.csv"

if not os.path.exists(file_path):
    print("❌ Dataset not found in this folder.")
    print("👉 Make sure 'amazon_reviews.csv' is in the same folder.")
    exit()

# Load dataset
df = pd.read_csv(file_path)

# Check data
print("Data loaded successfully!")
print(df.head())

# -----------------------------
# 📊 1. Rating Count Plot
# -----------------------------
plt.figure()
sns.countplot(x="rating", data=df)
plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# -----------------------------
# 📊 2. Histogram
# -----------------------------
plt.figure()
plt.hist(df["rating"], bins=5)
plt.title("Ratings Histogram")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()

# -----------------------------
# 📊 3. Box Plot
# -----------------------------
plt.figure()
sns.boxplot(x=df["rating"])
plt.title("Rating Spread")
plt.show()