# ================================================================
# DATA ANALYSIS CAPSTONE PROJECT
# ================================================================

# --- Importing Libraries (Toolkit) ---
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Importing & Inspecting Data ---
startups = pd.read_excel("datasets/startup-expansion.xlsx")

# Basic info
print(startups.info())
print(startups[["Marketing Spend", "Revenue"]].describe().round(2))

# --- Preprocessing Data ---
# Check unique cities
print("Unique Cities:", startups["City"].nunique())
print("Unique States:", startups["State"].nunique())

# Value counts
print(startups["State"].value_counts())
print(startups["Sales Region"].value_counts())
print(startups["New Expansion"].value_counts())

# Check for nulls and duplicates
print("Missing Values:\n", startups.isna().sum())
print("Duplicated Rows:", startups.duplicated().sum())

# --- Exploring & Analyzing Data ---
# Sample records
print(startups.sample(10))

# Sales region distribution
startups["Sales Region"].value_counts().plot.bar()
plt.title("Sales Region Distribution")
plt.show()

# Grouping by expansion
old_expansion_revenue = (
    startups[startups["New Expansion"] == "Old"]
    .groupby("State")["Revenue"]
    .sum()
    .nlargest(10)
)
print("Top 10 States by Revenue (Old Expansion):\n", old_expansion_revenue)

new_expansion_revenue = (
    startups[startups["New Expansion"] == "New"]
    .groupby("State")["Revenue"]
    .sum()
    .nlargest(10)
)
print("Top 10 States by Revenue (New Expansion):\n", new_expansion_revenue)

# --- Feature Engineering ---
# Profit
startups["Profit"] = startups["Revenue"] - startups["Marketing Spend"]

# Return on Marketing Spend (ROMS)
startups["ROMS"] = round(
    (startups["Profit"] / startups["Marketing Spend"]) * 100, 2
)
startups["ROMS%"] = startups["ROMS"] / 100

# Preview updated dataset
print(startups.head())

# --- Export Modified Data ---
startups.to_csv("startups-expansion-modified.csv", index=False)

# ================================================================
# END OF PROJECT
# ================================================================
