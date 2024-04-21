def generate_magic_square(n):

    if n % 2 == 0:
        raise ValueError("Magic square can only be generated for odd orders")

    magic_square = [[0] * n for a in range(n)]   #[0] * n creates a row of n number of zeroes in a single iteration
                                                    #  for a in range(n) iterates n times, creating a new row for each iteration.

    # Start position for 1
    i, j = n // 2, n - 1

    # Fill the magic square
    num = 1
    while num <= n * n:
        if i == -1 and j == n:  # Condition 4
            i, j = 0, n - 2
        else:
            # Condition 1
            if i < 0:
                i = n - 1
            if j == n:
                j = 0

            # Condition 3
            if magic_square[i][j] != 0:
                i, j = i + 1, j - 2

        magic_square[i][j] = num
        num += 1
        i, j = i - 1, j + 1

    return magic_square

def print_magic_square(square):
    for row in square:
        print(row)
while True:
    # Example usage for a 3x3 magic square
    n = int(input("Enter"))
    magic_square = generate_magic_square(n)
    print("Magic square of order", n, ":")
    print_magic_square(magic_square)
