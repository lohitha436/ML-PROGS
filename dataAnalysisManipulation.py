
import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

df['species'] = iris.target

print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nFiltered Data (Sepal Length > 6):")
filtered_data = df[df['sepal length (cm)'] > 6]
print(filtered_data)

print("\nMean values grouped by species:")
grouped_data = df.groupby('species').mean()
print(grouped_data)
