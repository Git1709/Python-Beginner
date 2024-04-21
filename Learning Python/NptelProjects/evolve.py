import random

# Reading the DNA file
with open("DNA_data.txt", "r") as myfile:  # Open the file for reading
    x = list(myfile.read())  # Read the file and convert it into a list

# Function to perform evolution
def evolve(X):
    for i in range(0, len(X)):  # Loop through each bit in the DNA
        # Generate random index and probability
        ind = random.randint(0, len(X) - 1)  # Generate random index
        P = random.randrange(1, 100,10)  # Generate random probability

        # Mutation based on random probability
        if P == 1:  # If the random probability is 1, then mutate
            if X[ind] == '0':  # If the bit at index 'ind' is '0', change it to '1'
                X[ind] = '1'
                print("Nice Job amigo :", P," at ",ind)
            else:  # Otherwise, change it to '0'
                X[ind] = '0'
                print("Nice Job amigo :", P, " at ", ind)
        else:
            print("Next try amigo :", P)

# Call the evolve function
evolve(x)

# Print the evolved DNA
print("Evolved DNA:", ''.join(x))
