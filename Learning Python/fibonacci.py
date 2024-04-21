#Using iteration

def fibonacci(n):
    fib_sequence = [0, 1]  # Initialize the Fibonacci sequence with the first two numbers
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]  # Add the last two numbers in the sequence
        fib_sequence.append(next_number)  # Append the next number to the sequence
    return fib_sequence[:n]  # Return the first n numbers of the Fibonacci sequence

# Example usage:
n = int(input(""))
print(fibonacci(n))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34,........]



#using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage:
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_sequence = [fibonacci(i) for i in range(n)]
print(fib_sequence)
