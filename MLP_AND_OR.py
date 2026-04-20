import numpy as np
from sklearn.linear_model import Perceptron

X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

y_and = [0,0,0,1]
y_or = [0,1,1,1]

# AND
model = Perceptron()
model.fit(X, y_and)
print("AND:", model.predict(X))

# OR
model.fit(X, y_or)
print("OR:", model.predict(X))
