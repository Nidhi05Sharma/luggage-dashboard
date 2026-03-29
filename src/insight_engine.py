import pandas as pd
import numpy as np

# Load cleaned dataset
df = pd.read_csv("luggage_dataset_final_clean.csv")


# ----------------------------
# STEP 1: PREP CLEAN DATA
# ----------------------------
df["review_count"] = df["review_count"].fillna(0)
df["rating"] = df["rating"].fillna(0)


# ----------------------------
# STEP 2: QUALITY SCORE
# quality_score = rating * log(review_count)
# ----------------------------
df["quality_score"] = df.apply(
    lambda row: row["rating"] * np.log(row["review_count"] + 1),
    axis=1
)


# ----------------------------
# STEP 3: BRAND EXTRACTION
# (Assumption: first word of title = brand)
# ----------------------------
df["brand"] = df["title"].apply(lambda x: str(x).split()[0])


# ----------------------------
# STEP 4: BRAND-WISE ANALYSIS
# ----------------------------
brand_stats = df.groupby("brand").agg(
    avg_price=("price", "mean"),
    avg_rating=("rating", "mean"),
    avg_quality=("quality_score", "mean"),
    product_count=("title", "count")
).reset_index()


# ----------------------------
# STEP 5: TOP 5 PRODUCTS
# ----------------------------
top_5_products = df.sort_values(
    by="quality_score",
    ascending=False
).head(5)


# ----------------------------
# STEP 6: BEST BRAND
# ----------------------------
best_brand = brand_stats.sort_values(
    by="avg_quality",
    ascending=False
).head(1)


# ----------------------------
# STEP 7: INSIGHT PRINTING
# ----------------------------
print("\n================ BRAND STATS ================\n")
print(brand_stats)

print("\n================ TOP 5 PRODUCTS ================\n")
print(top_5_products[["title", "price", "rating", "review_count", "quality_score"]])

print("\n================ BEST BRAND ================\n")
print(best_brand)


# ----------------------------
# STEP 8: SAVE OUTPUTS
# ----------------------------
brand_stats.to_csv("brand_analysis.csv", index=False)
top_5_products.to_csv("top_products.csv", index=False)

print("\nDONE → INSIGHT ENGINE OUTPUT CREATED")