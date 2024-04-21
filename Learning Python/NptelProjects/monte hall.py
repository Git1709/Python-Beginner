import random

def monte_hall_simulation(num_trials):
    swap_wins = 0
    no_swap_wins = 0

    for _ in range(num_trials):
        # Set up doors: 0 for goat, 1 for BMW
        doors = [0, 0, 1]

        # Shuffle the doors
        random.shuffle(doors)

        # Participant makes a choice
        choice = random.randint(0, 2)

        # Host opens a door with a goat behind it that wasn't chosen
        for i in range(3):
            if i != choice and doors[i] == 0:
                door_open = i
                break

        # Participant decides whether to swap or not
        swap = random.choice([True, False])

        # If swap is True, participant switches their choice
        if swap:
            for i in range(3):
                if i != choice and i != door_open:
                    choice = i
                    break

        # Check if the participant wins
        if doors[choice] == 1:
            if swap:
                swap_wins += 1
            else:
                no_swap_wins += 1

    return swap_wins, no_swap_wins

# Number of trials
num_trials = 10000

# Run the simulation
swap_wins, no_swap_wins = monte_hall_simulation(num_trials)

# Print results
print(f"Number of swap wins: {swap_wins}")
print(f"Number of no-swap wins: {no_swap_wins}")
