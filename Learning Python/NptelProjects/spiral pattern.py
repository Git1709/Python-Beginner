import turtle

def spiral_traversal(n):
    # Create n x n grid
    grid = [[0 for _ in range(n)] for _ in range(n)]

    # Define spiral traversal order
    dx = [0, 1, 0, -1]  # Change in row for each direction (right, down, left, up)
    dy = [1, 0, -1, 0]  # Change in column for each direction
    direction = 0  # Start moving right
    x, y = 0, 0  # Start from top-left corner

    # Iterate through the grid in spiral order
    for i in range(1, n * n + 1):
        grid[x][y] = i  # Display current cell

        # Calculate next position
        nx, ny = x + dx[direction], y + dy[direction]

        # Change direction if next position is out of bounds or already visited
        if nx < 0 or nx >= n or ny < 0 or ny >= n or grid[nx][ny] != 0:
            direction = (direction + 1) % 4  # Change direction (right -> down -> left -> up)
            nx, ny = x + dx[direction], y + dy[direction]

        x, y = nx, ny  # Move to next position

    # Return the grid with spiral traversal
    return grid

def print_spiral(matrix, turtle_obj):
    if not matrix:
        return

    # Define boundaries
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Print top row
        for i in range(left, right + 1):
            turtle_obj.write(matrix[top][i], align='center')
            turtle_obj.forward(20)

        top += 1
        turtle_obj.right(90)

        # Print rightmost column
        for i in range(top, bottom + 1):
            turtle_obj.write(matrix[i][right], align='center')
            turtle_obj.forward(20)

        right -= 1
        turtle_obj.right(90)

        # Print bottom row in reverse
        if top <= bottom:
            for i in range(right, left - 1, -1):
                turtle_obj.write(matrix[bottom][i], align='center')
                turtle_obj.forward(20)

            bottom -= 1
            turtle_obj.right(90)

        # Print leftmost column in reverse
        if left <= right:
            for i in range(bottom, top - 1, -1):
                turtle_obj.write(matrix[i][left], align='center')
                turtle_obj.forward(20)

            left += 1
            turtle_obj.right(90)
while True:# Example usage:
    n = int(input("Enter the size of matrix: "))
    matrix = spiral_traversal(n)

    # Set up Turtle
    wn = turtle.Screen()
    wn.setup(width=800, height=600)
    wn.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  # Set the fastest speed
    t.penup()   # Don't draw while moving
    t.goto(-150, 150)  # Set starting position

    # Print the spiral traversal
    print_spiral(matrix, t)

    wn.mainloop()
