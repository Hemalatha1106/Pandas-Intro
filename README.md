# 📘 Pandas – Study Documentation & Reference

This repository is a **self-study documentation project** created while learning **Pandas for Machine Learning and Data Analysis**.  
It includes commonly used functions, code snippets, explanations, and practical examples for quick revision and real-world usage.

🎯 **Goal:** Build strong fundamentals in Pandas for ML, data preprocessing, and analytics  
📂 **Type:** Study Notes + Code Reference + Hands-on Experiments  
🧠 **Focus Areas:** Data handling, filtering, aggregation, preprocessing, and dataset exploration  

---

## 📂 Repository Contents

- `main.py` → Important Pandas code snippets
- `pandasIntro.ipynb` → Hands-on practice & experiments
- `data/` → Sample datasets used for learning (ignored in Git if large)
- `.gitignore` → Excludes unnecessary folders like `venv/`, `data/` if required

---

## 🔍 Key Pandas Concepts & Functions

## 1. **Importing & Reading Data**
```python
import pandas as pd

df = pd.read_csv("file.csv")
```

## 2. Saving Data
```python
df.to_csv("output.csv", index=False)
```

## 3. Viewing Data
```python
df.head()
df.tail()
df.info()
df.describe()
df.shape
df.columns
```

## 4. Selecting Rows & Columns
```python
df["column"]                         # Single column
df[["col1", "col2"]]                 # Multiple columns
df.loc[2:5, ["col1", "col2"]]        # Label-based slicing
df.iloc[:, 1:4]                      # Position-based slicing
```                      

## 5. Filtering Data
```python
df[df["column"] > 50]
df[df["column"].isin(["A", "B"])]
df[(df["col1"] > 10) & (df["col2"] < 20)]
```

## 6. Grouping & Aggregation
```python
df.groupby("preferred_study_time")["leetcode_solved"].mean()
df.groupby("col").agg({"marks": "max", "age": "min"})
```

## 7. Sorting
```python
df.sort_values(by="leetcode_solved", ascending=False)
```

### 8. Handling Missing Values
```python
df.isnull().sum()
df.fillna(0, inplace=True)
df.dropna(inplace=True)
```

## 9. Adding & Removing Columns
```python
df["new_col"] = df["col1"] + df["col2"]
df.drop(columns=["new_col"], inplace=True)
```

## 10. Mapping Group Statistics to Rows
```python
group_avg = df.groupby("preferred_study_time")["leetcode_solved"].mean()
df["group_avg"] = df["preferred_study_time"].map(group_avg)
```
---

## 📌 Quick Notes

| Function | Purpose |
|--------|---------|
| `.loc` | Label-based selection |
| `.iloc` | Index-based (position) selection |
| `inplace=True` | Modifies the original DataFrame |
| `groupby()` | Returns Series/DataFrame, but does not sort automatically |
| `map()` | Assigns group results back to individual rows |

