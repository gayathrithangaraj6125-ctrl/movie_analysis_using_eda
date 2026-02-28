# 🎬 Movie Rating Analysis - Exploratory Data Analysis

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Pandas](https://img.shields.io/badge/Pandas-Latest-green)
![Seaborn](https://img.shields.io/badge/Seaborn-Latest-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

---

## 📌 About This Project

This is my first Data Science project where I performed 
Exploratory Data Analysis (EDA) on the TMDB 5000 Movies Dataset.
The goal of this project is to explore, clean, visualize, and 
find meaningful insights from real world movie data using Python.

This project is part of my Saturday Data Science learning journey
where I dedicate every Saturday evening to building real projects.

---

## 🎯 Objective

- Understand the structure and content of the TMDB Movies Dataset
- Clean the data by handling missing and zero values
- Visualize patterns and trends using charts
- Find key insights about movie ratings, budgets, revenue and popularity

---

## 📂 Dataset

- **Source:** [TMDB 5000 Movies Dataset - Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **File Used:** tmdb_5000_movies.csv
- **Total Records:** 4803 movies
- **Columns Used:** title, budget, revenue, vote_average, vote_count, popularity, release_date

---

## 🛠️ Tools and Technologies Used

| Tool | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data loading and manipulation |
| Numpy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Advanced data visualization |
| VS Code | Code editor |
| GitHub | Version control and portfolio |

---

## 📊 EDA Steps Performed

### 1. Data Loading
Loaded the CSV file using Pandas read_csv function

### 2. Data Exploration
- Checked first 5 rows using df.head()
- Checked shape of data using df.shape()
- Listed all column names using df.columns
- Checked missing values using df.isnull().sum()
- Got basic statistics using df.describe()

### 3. Data Cleaning
- Removed rows with missing values in important columns
- Removed movies with zero budget and zero revenue
- Converted release_date column to datetime format
- Extracted year from release_date

### 4. Data Visualization
Created 7 charts to find patterns in the data

---

## 📈 Charts Generated

| Chart | Description |

| Chart 1 | Distribution of Movie Ratings |
| Chart 2 | Top 10 Highest Rated Movies |
| Chart 3 | Top 10 Most Popular Movies |
| Chart 4 | Budget vs Rating |
| Chart 5 | Budget vs Revenue |
| Chart 6 | Movies Released Per Year |
| Chart 7 | Correlation Heatmap |

---

## 🔍 Key Insights Found

- Most movies are rated between 6.0 and 7.5 out of 10
- Higher budget does not always guarantee a higher rating
- Movies with higher budgets generally tend to earn more revenue
- Popularity score and rating are two different things entirely
- The number of movies produced has increased significantly over the years
- Vote count and popularity have a stronger correlation than budget and rating

---

## 📁 Project Structure
```
movie-rating-analysis/
│
├── tmdb_analysis.py       # Main Python code
├── README.md              # Project documentation
└── .gitignore             # Files to ignore in GitHub
```

---

## 🚀 How to Run This Project

### Step 1 - Clone this repository
```
git clone https://github.com/yourusername/movie-rating-analysis.git
```

### Step 2 - Install required libraries
```
pip install pandas numpy matplotlib seaborn
```

### Step 3 - Download the dataset
Download tmdb_5000_movies.csv from Kaggle and place it in the project folder

### Step 4 - Run the code
```
python tmdb_analysis.py
```

---

## 📚 What I Learned

- How to load and explore a real world dataset
- How to clean data by handling missing values
- How to create different types of charts using Matplotlib and Seaborn
- How to find and communicate insights from data
- How to use Git and GitHub for version control

---

## 👨‍💻 Author

**GAYATHRI THANGARAJ**
Prefinal Year Student
Aspiring Data Scientist

- GitHub: gayathrithangaraj6125-ctrl
- LinkedIn: https://www.linkedin.com/in/gayathri-thangaraj-808377328?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app

---

## ⭐ If you found this project helpful please give it a star on GitHub!
```

---

## 📌 How to Add This to Your Project

In VS Code terminal run:
```
git add README.md
git commit -m "Added README file"
git push
