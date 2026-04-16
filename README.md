# Airbnb Market Analysis: Berlin vs. Munich

This project provides a comparative analysis of Airbnb listing data for two major German cities: **Berlin** and **Munich**. It focuses on identifying market trends, pricing distributions, and revenue potential across different neighborhoods and room types using data from late 2025.

---

## 📊 Slides
https://drive.google.com/file/d/1LRtB7QbPn0vt_0VzZhebDQlx9XPgRAC6/view?usp=sharing

## 📊 Project Milestone: Data Refinement
Following a rigorous data refinement process, we have established a robust dataset of **14,759 records**. This high-volume sample provides a statistically significant foundation for our risk assessment models and market trend predictions.

---

## 🚀 Key Features
* **Remote Data Integration:** Automatically fetches the latest visualization datasets from *Inside Airbnb* for Berlin and Munich.
* **Data Standardization:** Merges disparate datasets into a unified structure for cross-city comparison.
* **Cleaning & Preprocessing:** Handles missing values, removes duplicates, and filters extreme price outliers to ensure data quality.
* **Revenue Modeling:** Estimates potential revenue per listing based on `price` and `minimum_nights` requirements.
* **Comparative Visualizations:** Generates insights into price frequency and total revenue distribution by room type.

---

## 🛠️ Technical Stack
* **Language:** Python
* **Data Manipulation:** `pandas`
* **Visualization:** `matplotlib`, `seaborn`
* **API Interface:** Custom `api.AirbnbRemoteData` module

---

## 📈 Key Insights
* **Pricing Distribution:** Analysis of the "sweet spot" in the market by excluding extreme outliers (listings > $1,000).
* **Revenue Leaders:** Identification of high-performing neighborhoods (e.g., *Alexanderplatz* in Berlin).
* **Supply Dynamics:** Direct comparison of neighborhood volume (Berlin's 138 neighborhoods vs. Munich's 25).

---

## 📂 Data Source
The analysis utilizes data from the following snapshots:
* **Berlin:** Listings as of September 23, 2025.
* **Munich:** Listings as of September 27, 2025.

---
