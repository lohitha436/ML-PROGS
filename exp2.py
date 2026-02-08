import numpy as np
import math
from scipy import stats

a = np.array([10, 20, 30])
b = np.array([2, 4, 6])

print("Addition:", np.add(a,b))
print("Subtraction:", np.subtract(a,b))
print("Multiplication:", np.multiply(a,b))
print("Division:", np.divide(a,b))
print("Exponentiation:", np.power(a,2))
print("Modulus:", np.mod(a,b))

print("Square root using math:", math.sqrt(25))
print("Mean using scipy:", stats.tmean(b))
