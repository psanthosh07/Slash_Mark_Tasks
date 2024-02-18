import random

def number_guessing_game():
    print("Welcome to the Unique Number Guessing Game!")
    print("Choose the range for the number.")

    while True:
        try:
            lower_bound = int(input("Enter the lower bound: "))
            upper_bound = int(input("Enter the upper bound: "))
            if lower_bound >= upper_bound:
                print("Please enter a valid range with lower bound smaller than the upper bound.")
            else:
                break
        except ValueError:
            print("Please enter valid integers for the bounds.")

    print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    while True:
        guess = input("Enter your guess (or 'q' to quit): ")

        if guess.lower() == 'q':
            print(f"The number was {secret_number}.")
            print("Thank you for playing!")
            break

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Try guessing higher.")
        else:
            print("Try guessing lower.")

number_guessing_game()
