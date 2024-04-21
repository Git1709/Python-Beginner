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

    # Display the grid with spiral traversal
    for row in grid:
        print(row)

# Example usage:
n = int(input("Enter"))
spiral_traversal(n)
