import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# load dataset
df = pd.read_csv("Mall_Customers.csv")

# select features
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# model
model = KMeans(n_clusters=3, random_state=42)
model.fit(X)

# add cluster labels
df['Cluster'] = model.labels_

# plot
# //all rows of 0th col,1st col
plt.scatter(X.iloc[:,0], X.iloc[:,1], c=model.labels_)
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.show()
#optional
from sklearn.metrics import silhouette_score
print("Score:", silhouette_score(X, model.labels_))
