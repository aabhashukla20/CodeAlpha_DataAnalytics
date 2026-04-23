import pandas as pd
from textblob import TextBlob

# -----------------------------
# 📁 Built-in Dataset
# -----------------------------
data = {
    "review": [
        "Great product, I loved it!",
        "Very bad quality",
        "Average experience",
        "Excellent service and fast delivery",
        "Worst product ever",
        "Good but could be better"
    ],
    "rating": [5, 1, 3, 5, 1, 3]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Dataset:")
print(df)

# -----------------------------
# 🔍 Sentiment Function
# -----------------------------
def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment
df["Sentiment"] = df["review"].apply(get_sentiment)

# -----------------------------
# 📊 Results
# -----------------------------
print("\nSentiment Results:")
print(df[["review", "Sentiment"]])

print("\nSentiment Count:")
print(df["Sentiment"].value_counts())

# Save output (optional)
df.to_csv("sentiment_output.csv", index=False)

print("\n✅ File saved as sentiment_output.csv")