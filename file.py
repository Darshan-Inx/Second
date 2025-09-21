import random

def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess the number.")

def get_player_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please guess a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def game():
    number_to_guess = random.randint(1, 100)
    attempts_left = 10
    guessed_correctly = False

    welcome_message()

    while attempts_left > 0 and not guessed_correctly:
        print(f"You have {attempts_left} attempts remaining.")
        guess = get_player_guess()

        if guess < number_to_guess:
            print("Too low! Try a higher number.")
        elif guess > number_to_guess:
            print("Too high! Try a lower number.")
        else:
            guessed_correctly = True
            print("Congratulations! You've guessed the correct number.")

        attempts_left -= 1

    if not guessed_correctly:
        print(f"Sorry! The correct number was {number_to_guess}.")

    elif not guessed_correctly:
        print("Sorry Brother.....")

    else:
        print("Not okay...")
if __name__ == "__main__":
    game()
