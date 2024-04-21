import turtle

# Function to traverse the matrix in spiral order
def spiral_traverse(matrix, n, m):
    k = 0
    l = 0

    # Initialize turtle
    screen = turtle.Screen()
    screen.setup(width=1000, height=800)
    screen.bgcolor("black")
    screen.title("Spiral Traversal")

    pen = turtle.Turtle()
    pen.speed(1000)
    pen.penup()
    pen.color("white")

    while k < n and l < m:
        # Print the first row from the remaining rows
        for i in range(l, m):
            pen.goto(50 * i, 50 * k)
            pen.dot(20)
            print(matrix[k][i], end=" ")

        k += 1

        # Print the last column from the remaining columns
        for i in range(k, n):
            pen.goto(50 * (m - 1), 50 * i)
            pen.dot(20)
            print(matrix[i][m - 1], end=" ")

        m -= 1

        # Print the last row from the remaining rows

        if k < n:
            for i in range(m - 1, l - 1, -1):
                pen.goto(50 * i, 50 * (n - 1))
                pen.dot(20)
                print(matrix[n - 1][i], end=" ")

            n -= 1

        # Print the first column from the remaining columns
        if l < m:
            for i in range(n - 1, k - 1, -1):
                pen.goto(50 * l, 50 * i)
                pen.dot(20)
                print(matrix[i][l], end=" ")

            l += 1

# Example matrix
matrix = [
    [1, 2, 3, 4, 5, 6, 7],
    [24, 25, 26, 27, 28, 29, 8],
    [23, 40, 41, 42, 43, 30, 9],
    [22, 39, 48, 49, 44, 31, 10],
    [21, 38, 47, 46, 45, 32, 11],
    [20, 37, 36, 35, 34, 33, 12],
    [19, 18, 17, 16, 15, 14, 13]
]

# Dimensions of the matrix
n = len(matrix)
m = len(matrix[0])

# Call the function to traverse the matrix in spiral order
spiral_traverse(matrix, n, m)

# Close the turtle graphics window when clicked
turtle.done()
