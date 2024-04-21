import random

def display_masked_gun():
    print("  _______  ")
    print(" /       \\ ")
    print("/   0 0   \\")
    print("|    ^    |")
    print(" \\_______/ ")

def generate_secret_code():
    return random.randint(1000, 9999)

def provide_feedback_and_manage_attempts(secret_code):
    attempts = 0
    max_attempts = 10
    while attempts < max_attempts:
        guess = input("Enter your 4-digit guess: ")
        if not guess.isdigit() or len(guess) != 4:
            print("Please enter a 4-digit numeric code.")
            continue

        guess = int(guess)
        if guess == secret_code:
            print("Congratulations! You've unlocked the masked gun!")
            return
        else:
            attempts += 1
            if attempts == max_attempts:
                print("Sorry, you've run out of attempts. The secret code was:", secret_code)
            else:
                print("Incorrect guess. Attempts left:", max_attempts - attempts)

print("Welcome to the Masked Gun game!")
print("Try to unlock the masked gun by guessing the 4-digit secret code.")

display_masked_gun()


secret_code = generate_secret_code()
provide_feedback_and_manage_attempts(secret_code)
