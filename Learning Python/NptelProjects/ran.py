import statistics
import matplotlib.pyplot as plt

# Sample data
data = [10, 20, 15, 25, 30, 12, 18, 22, 28, 35]

# Calculate statistics
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.mode(data)
stdev = statistics.stdev(data)

# Print statistics
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Standard Deviation:", stdev)

# Plot histogram
plt.hist(data, bins=5, color='skyblue', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Sample Data')
plt.axvline(mean, color='red', linestyle='dashed', linewidth=1, label='Mean')
plt.axvline(median, color='green', linestyle='dashed', linewidth=1, label='Median')
plt.legend()
plt.show()
