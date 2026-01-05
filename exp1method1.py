import math
# Input data
data = list(map(int, input("Enter numbers separated by space: ").split()))
n = len(data)

#  Mean
total = 0
for x in data:
    total += x
mean = total / n

# Median
data.sort()

if n % 2 == 0:
    median = (data[n//2 - 1] + data[n//2]) / 2
else:
    median = data[n//2]

# Mode
freq = {}

for x in data:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

max_freq = 0
for value in freq.values():
    if value > max_freq:
        max_freq = value

if max_freq == 1:
    mode = "No unique mode"
else:
    mode = []
    for key, value in freq.items():
        if value == max_freq:
            mode.append(key)

# Variance
variance_sum = 0
for x in data:
    variance_sum += (x - mean) ** 2

variance = variance_sum / n   # Population variance

# Standard Deviation
std_deviation = math.sqrt(variance)

print("\nResults:")
print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)
print("Variance =", variance)
print("Standard Deviation =", std_deviation)
