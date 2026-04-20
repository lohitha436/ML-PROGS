import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
df=pd.read_csv(r"/content/Salary_dataset.csv")
df.head()

X=df[['YearsExperience']]
y=df['Salary']

model=LinearRegression()
model.fit(X, y)
y_pred=model.predict(X)
plt.scatter(X,y)
plt.plot(X,y_pred)
plt.show()
print("r2 score: ",r2_score(y,y_pred))
