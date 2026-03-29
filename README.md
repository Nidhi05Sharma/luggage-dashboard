🧳 Luggage Market Intelligence Dashboard
📌 Project Overview

This project is an end-to-end product intelligence system built on Amazon India luggage data.

It transforms unstructured marketplace data into decision-ready insights by combining:

Web scraping
Data cleaning & structuring
Analytical scoring
AI-driven insights
Interactive dashboard

The goal is to simulate how a business can compare brands, understand customer sentiment, and identify which products deliver the best value.

🎯 Problem Statement

E-commerce platforms contain large amounts of unstructured and noisy data (prices, ratings, reviews).

This project answers:

Which luggage brands are performing better, and why?

📁 Project Structure
luggage-dashboard/
│
├── src/
│   ├── scraper/
│   │   └── amazon_scraper.py
│   │
│   ├── analysis/
│   │   ├── insight_engine.py
│   │   └── ai_insights.py
│
├── app/
│   └── app.py
│
├── data/
│   └── luggage_dataset_final_clean.csv
│
├── requirements.txt
└── README.md
⚙️ Tech Stack
Python
Pandas, NumPy
BeautifulSoup + Requests (Scraping)
Streamlit (Dashboard)
🔄 Pipeline Flow
Scraping → Cleaning → Analysis → AI Layer → Dashboard
📊 Key Features
🔹 1. Multi-Brand Data Collection

Scraped product data from:

Safari
VIP
Aristocrat
American Tourister

Each product includes:

Title
Price
Rating
Review count
🔹 2. Data Cleaning & Structuring
Standardized price, rating, and review formats
Removed inconsistencies and handled missing values
Created a structured dataset for downstream analysis
🔹 3. Insight Engine

Built analytical metrics using Pandas:

✅ Quality Score
quality_score = rating × log(review_count + 1)

This captures both:

product rating
review reliability (trust signal)

Generated:

Top product rankings
Brand-level comparisons
Price vs rating insights
🔹 4. AI / Intelligence Layer

Implemented a lightweight AI layer to extract meaning from reviews:

Sentiment scoring
Pros & cons extraction
Value-for-money metric
✅ Value Score
value_score = sentiment_score / price

This helps identify products that balance cost and customer satisfaction.

🔹 5. Interactive Dashboard (Streamlit)

The dashboard provides:

📊 Dataset exploration
📈 Key metrics (avg price, rating, counts)
🏷 Brand comparison view
🏆 Top product rankings
🔍 Filters (brand, price range)
🤖 AI insights (sentiment, pros/cons, agent insights)
💡 Key Insights
Higher price does not always correlate with better customer sentiment
Products with more reviews tend to have more reliable ratings
Mid-range products often show durability-related complaints
Discount-heavy products show mixed satisfaction trends
Value-for-money products balance moderate pricing with positive sentiment
⚠️ Limitations
Review extraction is limited due to Amazon’s dynamic structure
Dataset size is controlled for reliability and speed
Sentiment analysis is rule-based (not deep NLP)
🔮 Future Improvements
Use advanced NLP/LLM for deeper sentiment and theme extraction
Automate large-scale scraping across more products
Add anomaly detection (e.g., high rating but negative themes)
Deploy dashboard as a live web application
🚀 How to Run
1. Install dependencies
pip install -r requirements.txt
2. Run the dashboard
streamlit run app/app.py
🧠 Final Note

This project goes beyond basic data extraction and focuses on:

Explaining why certain products and brands perform better using structured data and AI-driven insights.