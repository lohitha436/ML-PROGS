# Import required libraries
import pandas as pd
from sklearn.datasets import load_iris

# Load dataset
iris = load_iris()

# Convert dataset into Pandas DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add target column
df['species'] = iris.target

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Dataset information
print("\nDataset Information:")
print(df.info())

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Filter data
print("\nFiltered Data (Sepal Length > 6):")
filtered_data = df[df['sepal length (cm)'] > 6]
print(filtered_data)

# Group data by species and calculate mean
print("\nMean values grouped by species:")
grouped_data = df.groupby('species').mean()
print(grouped_data)
