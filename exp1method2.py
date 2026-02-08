# Method 2:
import statistics
data = list(map(int, input("Enter numbers separated by space: ").split()))

mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
variance = statistics.variance(data)
std_dev = statistics.stdev(data)

print("\nResults:")
print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)
print("Variance =", variance)
print("Standard Deviation =", std_dev)
