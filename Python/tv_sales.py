# IMPORT LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Sales CSV
df = pd.read_csv("Data/tv_sales2.csv")

# Preview Data
print(df.head())
print(df.info())
print(df.describe())


# DATA CLEANING


# Check missing values
print("Missing values per column:\n", df.isna().sum())

# Fill missing values
df = df.fillna(0)

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])


# BASIC ANALYSIS


# 1️Revenue by TV Brand (Product Category equivalent)
sales_by_product = df.groupby("TV_Brand")["Revenue"].sum().reset_index()

plt.figure(figsize=(10,6))
sns.barplot(x="TV_Brand", y="Revenue", data=sales_by_product)
plt.title("Total Revenue by TV Brand")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# SALES TREND OVER TIME

sales_trend = df.groupby("Date")["Revenue"].sum().reset_index()

plt.figure(figsize=(12,6))
sns.lineplot(x="Date", y="Revenue", data=sales_trend)
plt.title("Revenue Trend Over Time")
plt.xticks(rotation=40)
plt.tight_layout()
plt.show()


# TOP SELLING PRODUCTS


top_products = (
    df.groupby("Model")["Units_Sold"]
    .sum()
    .reset_index()
    .sort_values(by="Units_Sold", ascending=False)
    .head(10)
)

plt.figure(figsize=(10,6))
sns.barplot(x="Units_Sold", y="Model", data=top_products)
plt.title("Top 10 Best-Selling TV Models")
plt.tight_layout()
plt.show()


# SAVE CLEANED DATA FOR BI


df.to_csv("Data/tv_sales2_cleaned.csv", index=False)
print("Cleaned dataset saved for Power BI.")
