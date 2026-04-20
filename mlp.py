import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# load dataset
df = pd.read_csv("Housing.csv")

# features and target
X=df[['area' ,'bedrooms','parking']]
y=df['price']
# split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# model
model = Sequential()
model.add(Dense(10, input_dim=3, activation='relu'))
model.add(Dense(5, activation='relu'))
model.add(Dense(1))  # output layer

# compile
model.compile(optimizer='adam', loss='mse')

# train
model.fit(X_train, y_train, epochs=100, verbose=0)

# prediction
y_pred = model.predict(X_test)

# accuracy
print("R2 Score:", r2_score(y_test, y_pred))
