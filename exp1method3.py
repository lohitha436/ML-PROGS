import pandas as pd
from sklearn.datasets import load_wine
from statistics import mean, median, mode, variance, stdev

# Import dataset
data = load_wine()
df = pd.DataFrame(data.data, columns=data.feature_names)

# Select one column
values = df['alcohol']

print("Mean:", mean(values))
print("Median:", median(values))
print("Mode:", mode(values))
print("Variance:", variance(values))
print("Standard Deviation:", stdev(values))
