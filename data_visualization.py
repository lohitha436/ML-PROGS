# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()

# Convert dataset into Pandas DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Line Plot
plt.plot(df['sepal length (cm)'])
plt.title("Line Plot of Sepal Length")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.show()

# Scatter Plot
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'], c=df['species'])
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.show()
