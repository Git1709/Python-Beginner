def final(n, moves):
    x, y = 1, 1  # Starting position

    for move in moves:
        if move == "N" and y < n:
            y += 1
        elif move == "E" and x < n:
            x += 1
        elif move == "W" and x > 1:
            x -= 1
        elif move == "S" and y > 1:
            y -= 1

    return (x, y)
