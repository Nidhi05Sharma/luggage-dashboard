import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import numpy as np

# ✅ AI IMPORT
from src.analysis.ai_insights import apply_ai_insights, get_agent_insights


# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(page_title="Luggage Dashboard", layout="wide")
st.title("🧳 Luggage Market Intelligence Dashboard")


# ----------------------------
# LOAD DATA
# ----------------------------
df = pd.read_csv("data/luggage_dataset_final_clean.csv")


# ----------------------------
# FIX DATA TYPES (FINAL FIX)
# ----------------------------

# PRICE FIX (handles ₹, commas, dots)
df["price"] = (
    df["price"]
    .astype(str)
    .str.replace(",", "")
    .str.replace("₹", "")
    .str.replace(".", "", regex=False)
)
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# RATING FIX
df["rating"] = (
    df["rating"]
    .astype(str)
    .str.extract(r"(\d+\.?\d*)")[0]
)
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

# REVIEW COUNT FIX
df["review_count"] = (
    df["review_count"]
    .astype(str)
    .str.replace(",", "")
    .str.replace("(", "")
    .str.replace(")", "")
)
df["review_count"] = pd.to_numeric(df["review_count"], errors="coerce").fillna(0)


# ----------------------------
# BRAND COLUMN (if missing)
# ----------------------------
if "brand" not in df.columns:
    df["brand"] = df["title"].apply(lambda x: str(x).split()[0])


# ----------------------------
# QUALITY SCORE
# ----------------------------
df["quality_score"] = df.apply(
    lambda row: row["rating"] * np.log(row["review_count"] + 1),
    axis=1
)


# ----------------------------
# FIX REVIEWS COLUMN FOR AI
# ----------------------------
if "sample_reviews" not in df.columns:
    if "reviews" in df.columns:
        df["sample_reviews"] = df["reviews"].apply(
            lambda x: "No reviews available" if str(x) == "[]" else str(x)
        )
    else:
        df["sample_reviews"] = "No reviews available"


# ----------------------------
# APPLY AI LAYER
# ----------------------------
df = apply_ai_insights(df)


# ----------------------------
# SIDEBAR FILTERS
# ----------------------------
st.sidebar.header("Filters")

brand_list = df["brand"].dropna().unique().tolist()
selected_brand = st.sidebar.selectbox("Select Brand", ["All"] + brand_list)

min_price, max_price = int(df["price"].min()), int(df["price"].max())
price_range = st.sidebar.slider(
    "Price Range", min_price, max_price, (min_price, max_price)
)


# ----------------------------
# APPLY FILTERS
# ----------------------------
filtered_df = df.copy()

if selected_brand != "All":
    filtered_df = filtered_df[filtered_df["brand"] == selected_brand]

filtered_df = filtered_df[
    (filtered_df["price"] >= price_range[0]) &
    (filtered_df["price"] <= price_range[1])
]


# ----------------------------
# SECTION 1: DATASET VIEW
# ----------------------------
st.subheader("📊 Dataset View")
st.dataframe(filtered_df)


# ----------------------------
# SECTION 2: KPIs
# ----------------------------
st.subheader("📈 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Products", len(filtered_df))
col2.metric("Avg Rating", round(filtered_df["rating"].mean(), 2))
col3.metric("Avg Price", round(filtered_df["price"].mean(), 2))


# ----------------------------
# SECTION 3: BRAND ANALYTICS
# ----------------------------
st.subheader("🏷 Brand Analytics")

brand_stats = filtered_df.groupby("brand").agg(
    avg_price=("price", "mean"),
    avg_rating=("rating", "mean"),
    product_count=("title", "count")
).reset_index()

st.dataframe(brand_stats)


# ----------------------------
# SECTION 4: TOP PRODUCTS
# ----------------------------
st.subheader("🏆 Top Products")

top_products = filtered_df.sort_values(
    by="quality_score",
    ascending=False
).head(5)

st.dataframe(
    top_products[["title", "price", "rating", "review_count", "quality_score"]]
)


# ----------------------------
# AI SECTION: PREVIEW
# ----------------------------
st.subheader("📊 AI Insights Preview")

st.dataframe(
    filtered_df[["brand", "price", "rating", "sentiment_score", "value_score"]]
)


# ----------------------------
# AI SECTION: PROS / CONS
# ----------------------------
st.subheader("🧠 Product Insights")

st.dataframe(
    filtered_df[["title", "pros", "cons"]]
)


# ----------------------------
# AI SECTION: AGENT INSIGHTS
# ----------------------------
st.subheader("🤖 Agent Insights")

insights = get_agent_insights()

for insight in insights:
    st.write("•", insight)


# ----------------------------
# FINAL INSIGHT BOX
# ----------------------------
st.subheader("💡 Insight")

st.info(
    "Multi-brand analysis enabled. Quality score combines rating and review volume, "
    "providing a more reliable product ranking than rating alone."
)