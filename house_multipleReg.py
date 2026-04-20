import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
df=pd.read_csv(r"/content/Housing.csv")
df.head()

X=df[['area' ,'bedrooms','parking']]
y=df['price']

model=LinearRegression()
model.fit(X, y)
y_pred=model.predict(X)
plt.scatter(y, y_pred)
plt.plot(y, y)   # straight line
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted")
plt.show()
print("r2 score: ",r2_score(y,y_pred))
