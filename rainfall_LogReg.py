import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# load dataset
df = pd.read_csv("weatherAUS.csv")

# remove missing values
df = df.dropna()

# convert Yes/No → 1/0
df['RainTomorrow'] = df['RainTomorrow'].map({'Yes': 1, 'No': 0})

# features and target
X = df[['MinTemp', 'MaxTemp', 'Humidity9am']]
y = df['RainTomorrow']

# split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# prediction
y_pred = model.predict(X_test)

# accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))
