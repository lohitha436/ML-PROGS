import pandas as pd
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

df = pd.read_csv("daily_weather.csv")
df = df.dropna()

X = df.drop('relative_humidity_3pm', axis=1)
y = df['relative_humidity_3pm']

# split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# model
model = DecisionTreeRegressor(max_depth=3)
model.fit(X_train, y_train)

# prediction
y_pred = model.predict(X_test)

# accuracy
print("R2 Score:", r2_score(y_test, y_pred))

# 🌳 plot tree
plt.figure(figsize=(12,6))
plot_tree(model, feature_names=X.columns, filled=True)
plt.show()
