import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/students.csv")

# Encode categorical
le = LabelEncoder()
df["preferred_study_time"] = le.fit_transform(df["preferred_study_time"])

# Select features for clustering
final_df = df[[
    "study_hours_per_week",
    "leetcode_solved",
    "days_active",
    "preferred_study_time",
    "project_count",
    "hackathon_participation",
    "topic_count"
]].copy()

# Apply KMeans
kmeans = KMeans(n_clusters=4, random_state=42)
final_df["cluster"] = kmeans.fit_predict(final_df)

print("\nCluster assignments:")
print(final_df["cluster"].value_counts())

# PCA visualize
pca = PCA(n_components=2)
reduced = pca.fit_transform(final_df.drop("cluster", axis=1))

plt.scatter(reduced[:, 0], reduced[:, 1], c=final_df["cluster"])
plt.title("Student Study Clusters")
plt.show()

# Show students per cluster
for i in range(4):
    print(f"\nCluster {i}:")
    print(df.iloc[final_df[final_df["cluster"] == i].index]["name"].tolist())
