import random

# Using randint to generate random integer between 1 and 5 (inclusive)
random_int = random.randint(1, 5)
print("Random integer between 1 and 5:", random_int)

# Using randrange to generate random integer between 1 and 5 (inclusive)
random_int_range = random.randrange(1, 6)
print("Random integer between 1 and 5 using randrange:", random_int_range)

# Using random to generate random floating-point number between 0 and 1
random_float = random.random()
print("Random floating-point number between 0 and 1:", random_float)

# Using randrange with step to generate only odd numbers between 1 and 9
random_odd = random.randrange(1, 10, 2)
print("Random odd number between 1 and 9:", random_odd)

# Using randrange with step to generate only even numbers between 2 and 10
random_even = random.randrange(2, 12, 2)
print("Random even number between 2 and 10:", random_even)

# Using choice to select a random element from a list
my_list = [1, 2, 3, 4]
random_choice = random.choice(my_list)
print("Random choice from list:", random_choice)
