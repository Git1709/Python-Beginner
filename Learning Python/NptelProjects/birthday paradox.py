import random

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def generate_birth_date():
    month = random.randint(1, 12)
    if month == 2:  # February
        year = random.randint(1900, 2022)  # Choose a year between 1900 and 2022
        if is_leap_year(year):
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)
    elif month in [4, 6, 9, 11]:  # April, June, September, November
        day = random.randint(1, 30)
    else:  # January, March, May, July, August, October, December
        day = random.randint(1, 31)
    return month, day

def check_for_collision(birth_dates):
    seen = set()
    for date in birth_dates:
        if date in seen:
            return True
        seen.add(date)
    return False

def simulate_birthday_paradox(num_people, num_simulations):
    collisions = 0
    for _ in range(num_simulations):
        birth_dates = [generate_birth_date() for _ in range(num_people)]
        if check_for_collision(birth_dates):
            collisions += 1
    collision_probability = collisions / num_simulations
    print(f"Number of people: {num_people}")
    print(f"Number of simulations: {num_simulations}")
    print(f"Probability of a collision: {collision_probability:.4f}")

# Example usage
num_people = 9
num_simulations = 10000
simulate_birthday_paradox(num_people, num_simulations)

print("---------------------------------------")

import datetime

# Display today's date
aj=datetime.date
today_date = aj.today()
print("Today's date:", today_date)

# Segregate date components
year = today_date.strftime("%Y")
month = today_date.strftime("%B")
day = today_date.strftime("%d")
print("Year:", year)
print("Month:", month)
print("Day:", day)

# Week number of the year
week_number_year = today_date.strftime("%W")
print("Week number of the year:", week_number_year)

# Week number of the month
week_number_month = today_date.strftime("%W")
print("Week number of the month:", week_number_month)

# Weekday      A is the keyword
weekday = today_date.strftime("%A")
print("Weekday:", weekday)

# Day of the year
day_of_year = today_date.strftime("%j")
print("Day of the year:", day_of_year)

# Current time
current_time = datetime.datetime.now().strftime("%H:%M:%S")
print("Current time:", current_time)
