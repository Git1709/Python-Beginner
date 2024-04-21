import matplotlib.pyplot as plt

def ssort(x):
    steps = []
    for i in range(len(x)):
        for j in range((i+1),len(x)):
            if x[i] < x[j]:
                x[i], x[j] = x[j], x[i]
                steps.append(x[:])  # Record the current state of the list after each swap
    return x, steps

# Sample list for demonstration
x = [4, 2, 7, 1, 9, 3]

# Perform sorting and get steps for visualization
y, steps = ssort(x)

# Plotting the steps
for i, step in enumerate(steps):
    plt.bar(range(len(step)), step)
    plt.title(f"Step {i+1}")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.show()

# Calculate median
if len(y) % 2 == 0:
    median = (y[int(len(y)/2)] + y[int(len(y)/2) - 1]) / 2
    print("Median is ", median)
else:
    median = y[int(len(y)//2)]
    print("Median is", median)
