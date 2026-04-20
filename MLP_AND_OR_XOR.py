import numpy as np
from sklearn.neural_network import MLPClassifier

# Input
X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

# Outputs
y_and = np.array([0,0,0,1])
y_or = np.array([0,1,1,1])
y_xor = np.array([0,1,1,0])

# Model (FIXED)
model = MLPClassifier(hidden_layer_sizes=(2,),
                      activation='logistic',
                      max_iter=5000,
                      random_state=1)

# AND
model.fit(X, y_and)
print("AND Predictions:", model.predict(X))

# OR
model.fit(X, y_or)
print("OR Predictions:", model.predict(X))

# XOR
model.fit(X, y_xor)
print("XOR Predictions:", model.predict(X))
