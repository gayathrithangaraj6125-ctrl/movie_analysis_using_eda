# ============================================
# 🎬 TMDB Movie Rating Analysis - Real Dataset
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# ============================================
# STEP 1: Load the Real Dataset
# ============================================

df = pd.read_csv('tmdb_5000_movies.csv')

print("=" * 50)
print("✅ Dataset Loaded Successfully!")
print("=" * 50)

# ============================================
# STEP 2: First Look at the Data
# ============================================

print("\n📋 First 5 rows:")
print(df.head())

print("\n📐 Shape (rows, columns):", df.shape)

print("\n🏷️ Column Names:")
print(df.columns.tolist())

print("\n❓ Missing Values:")
print(df.isnull().sum())

print("\n📊 Basic Statistics:")
print(df.describe())

# ============================================
# STEP 3: Clean the Data
# ============================================

# Remove rows where important columns are empty or zero
df = df.dropna(subset=['vote_average', 'budget', 'revenue'])
df = df[df['budget'] > 0]
df = df[df['revenue'] > 0]
df = df[df['vote_average'] > 0]

print("\n✅ After Cleaning - Shape:", df.shape)

# ============================================
# STEP 4: Chart 1 - Rating Distribution
# ============================================

plt.figure()
sns.histplot(df['vote_average'], bins=20, kde=True, color='steelblue')
plt.title('📊 Distribution of Movie Ratings', fontsize=16)
plt.xlabel('Rating (out of 10)')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('chart1_rating_distribution.png')
plt.show()
print("✅ Chart 1 saved!")

# ============================================
# STEP 5: Chart 2 - Top 10 Highest Rated Movies
# ============================================

plt.figure()
top10 = df.nlargest(10, 'vote_average')[['title', 'vote_average']]
sns.barplot(data=top10, x='vote_average', y='title', palette='viridis')
plt.title('🏆 Top 10 Highest Rated Movies', fontsize=16)
plt.xlabel('Rating')
plt.ylabel('Movie Title')
plt.tight_layout()
plt.savefig('chart2_top10_movies.png')
plt.show()
print("✅ Chart 2 saved!")

# ============================================
# STEP 6: Chart 3 - Top 10 Most Popular Movies
# ============================================

plt.figure()
top10_popular = df.nlargest(10, 'popularity')[['title', 'popularity']]
sns.barplot(data=top10_popular, x='popularity', y='title', palette='magma')
plt.title('🔥 Top 10 Most Popular Movies', fontsize=16)
plt.xlabel('Popularity Score')
plt.ylabel('Movie Title')
plt.tight_layout()
plt.savefig('chart3_top10_popular.png')
plt.show()
print("✅ Chart 3 saved!")

# ============================================
# STEP 7: Chart 4 - Budget vs Rating
# ============================================

plt.figure()
sns.scatterplot(data=df, x='budget', y='vote_average', alpha=0.5, color='tomato')
plt.title('💰 Budget vs Rating', fontsize=16)
plt.xlabel('Budget ($)')
plt.ylabel('Rating')
plt.tight_layout()
plt.savefig('chart4_budget_vs_rating.png')
plt.show()
print("✅ Chart 4 saved!")

# ============================================
# STEP 8: Chart 5 - Budget vs Revenue
# ============================================

plt.figure()
sns.scatterplot(data=df, x='budget', y='revenue', alpha=0.5, color='green')
plt.title('💵 Budget vs Revenue', fontsize=16)
plt.xlabel('Budget ($)')
plt.ylabel('Revenue ($)')
plt.tight_layout()
plt.savefig('chart5_budget_vs_revenue.png')
plt.show()
print("✅ Chart 5 saved!")

# ============================================
# STEP 9: Chart 6 - Movies Released Per Year
# ============================================

plt.figure()
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
df['year'] = df['release_date'].dt.year
movies_per_year = df['year'].value_counts().sort_index()
sns.lineplot(x=movies_per_year.index, y=movies_per_year.values, color='purple')
plt.title('📅 Movies Released Per Year', fontsize=16)
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.tight_layout()
plt.savefig('chart6_movies_per_year.png')
plt.show()
print("✅ Chart 6 saved!")

# ============================================
# STEP 10: Chart 7 - Correlation Heatmap
# ============================================

plt.figure()
numeric_cols = df[['vote_average', 'vote_count', 'budget', 'revenue', 'popularity']]
sns.heatmap(numeric_cols.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('🔥 Correlation Heatmap', fontsize=16)
plt.tight_layout()
plt.savefig('chart7_heatmap.png')
plt.show()
print("✅ Chart 7 saved!")

# ============================================
# STEP 11: Key Insights Summary
# ============================================

print("\n" + "=" * 50)
print("🏆 KEY INSIGHTS FROM THE DATA")
print("=" * 50)
print(f"⭐ Highest rated movie  : {df.loc[df['vote_average'].idxmax(), 'title']} ({df['vote_average'].max()})")
print(f"💀 Lowest rated movie   : {df.loc[df['vote_average'].idxmin(), 'title']} ({df['vote_average'].min()})")
print(f"💰 Biggest budget movie : {df.loc[df['budget'].idxmax(), 'title']} (${df['budget'].max():,.0f})")
print(f"💵 Highest revenue movie: {df.loc[df['revenue'].idxmax(), 'title']} (${df['revenue'].max():,.0f})")
print(f"🔥 Most popular movie   : {df.loc[df['popularity'].idxmax(), 'title']}")
print(f"🎯 Average rating       : {df['vote_average'].mean():.2f}")
print(f"📦 Total movies analyzed: {len(df)}")
