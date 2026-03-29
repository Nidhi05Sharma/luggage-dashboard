import pandas as pd

# Load raw dataset
df = pd.read_csv("luggage_dataset_clean.csv")


def clean_price(price):
    if pd.isna(price):
        return None

    price = str(price).replace("₹", "").replace(",", "").strip()

    # remove trailing dot like "1899."
    if price.endswith("."):
        price = price[:-1]

    try:
        return int(price)
    except:
        return None


def clean_rating(rating):
    try:
        return float(str(rating).split(" ")[0])
    except:
        return None


def clean_review_count(rc):
    try:
        return int(str(rc).replace(",", "").replace("(", "").replace(")", "").strip())
    except:
        return 0


def build_sample_reviews(reviews):
    if pd.isna(reviews) or reviews == "[]":
        return "No reviews available"
    return str(reviews)[:300]


cleaned_data = []

for _, row in df.iterrows():

    price = clean_price(row["price"])
    rating = clean_rating(row["rating"])
    review_count = clean_review_count(row["review_count"])
    reviews = row["reviews"]

    # ✅ only skip if REALLY broken
    if price is None:
        continue

    cleaned_product = {
        "title": row["title"],
        "price": price,
        "rating": rating if rating else 0,
        "review_count": review_count,
        "sample_reviews": build_sample_reviews(reviews),
        "avg_review_length": len(str(reviews)) if reviews != "[]" else 0
    }

    cleaned_data.append(cleaned_product)


clean_df = pd.DataFrame(cleaned_data)

print("\nCLEAN DATASET READY:\n")
print(clean_df)

clean_df.to_csv("luggage_dataset_final_clean.csv", index=False)

print("\nDONE → FINAL CLEAN FILE CREATED")