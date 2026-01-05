# Import required libraries
import numpy as np
import math
import statistics as stats
from scipy import special

# Define two arrays
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([2, 4, 5, 8, 10])

# Arithmetic Operations using NumPy
addition = np.add(array1, array2)
subtraction = np.subtract(array1, array2)
multiplication = np.multiply(array1, array2)
division = np.divide(array1, array2)
modulus = np.mod(array1, array2)

# Exponentiation
# Using NumPy
exponent_numpy = np.power(array1, 2)

# Using Math (applied element-wise)
exponent_math = [math.pow(x, 2) for x in array1]

# Using SciPy
exponent_scipy = special.exp2(array2)  # 2^x for each element

# Statistics operations
mean_array1 = stats.mean(array1)
median_array1 = stats.median(array1)

# Display results
print("Array 1:", array1)
print("Array 2:", array2)

print("\nAddition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)

print("\nExponentiation (NumPy - array1^2):", exponent_numpy)
print("Exponentiation (Math - array1^2):", exponent_math)
print("Exponentiation (SciPy - 2^array2):", exponent_scipy)

print("\nStatistics on Array 1:")
print("Mean:", mean_array1)
print("Median:", median_array1)
