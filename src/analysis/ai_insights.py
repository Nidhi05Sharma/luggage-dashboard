import pandas as pd

# ----------------------------
# SENTIMENT FUNCTION
# ----------------------------
def get_sentiment(text):
    positive_words = ["good", "great", "durable", "smooth", "lightweight"]
    negative_words = ["bad", "poor", "broken", "zipper", "wheel", "issue"]

    score = 0
    text = str(text).lower()

    for word in positive_words:
        if word in text:
            score += 1

    for word in negative_words:
        if word in text:
            score -= 1

    return score


# ----------------------------
# PROS / CONS EXTRACTION
# ----------------------------
def extract_pros_cons(text):
    text = str(text).lower()

    pros = []
    cons = []

    if "durable" in text:
        pros.append("durable")
    if "lightweight" in text:
        pros.append("lightweight")
    if "smooth" in text:
        pros.append("smooth wheels")

    if "zipper" in text:
        cons.append("zipper issue")
    if "wheel" in text:
        cons.append("wheel issue")
    if "broken" in text:
        cons.append("durability issue")

    return ", ".join(pros), ", ".join(cons)


# ----------------------------
# APPLY AI INSIGHTS
# ----------------------------
def apply_ai_insights(df):

    df["sentiment_score"] = df["sample_reviews"].apply(get_sentiment)

    pros_cons = df["sample_reviews"].apply(extract_pros_cons)
    df["pros"] = pros_cons.apply(lambda x: x[0])
    df["cons"] = pros_cons.apply(lambda x: x[1])

    df["value_score"] = df["sentiment_score"] / (df["price"] + 1)

    return df


# ----------------------------
# AGENT INSIGHTS
# ----------------------------
def get_agent_insights():

    return [
        "Higher price does not always correlate with better sentiment.",
        "Products with more reviews tend to provide more reliable ratings.",
        "Some mid-range products show recurring durability complaints.",
        "Discount-heavy products often show mixed customer satisfaction.",
        "Value-for-money products balance moderate pricing with positive sentiment."
    ]