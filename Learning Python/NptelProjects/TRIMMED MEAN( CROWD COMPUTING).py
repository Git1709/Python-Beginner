from scipy import stats
from  statistics import mean
import matplotlib.pyplot as plt
# Example dataset
data = [10, 15, 12, 8, 20, 9, 7, 13, 14, 16]

# Step 1: Sort the Data
sorted_data = sorted(data)

# Step 2: Determine the Trimming Percentage
trim_percentage = float(input("Enter a trim value in percentage "))
trim_percentage = trim_percentage / 100

# Step 3: Identify the Number of Values to Trim
num_values_to_trim = int(len(sorted_data) * trim_percentage)

# Step 4: Remove the Trimmed Values
if trim_percentage < 0.1:
         trimmed_data = sorted_data[1:-1]  # Trim only one element from each side
else:
        trimmed_data = sorted_data[num_values_to_trim:-num_values_to_trim]

# Check if there are any data points remaining after trimming
if trimmed_data:
    # Step 5: Calculate the Mean
     trimmed_mean = stats.trim_mean(sorted_data, trim_percentage)
     mean = mean(trimmed_data)

     print("Trimmed Mean:", trimmed_mean)
     print("Mean:", mean)
     plt.plot(trimmed_data,'r.')
     plt.xlabel('Index')
     plt.ylabel('Value')
     plt.title('Plot of Trimmed Data')
     plt.show()

else:
         print("After trimming, there are no data points remaining.")
