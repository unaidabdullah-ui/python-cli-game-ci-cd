import random

def play_game():
    print("Welcome to the Guessing Game!")
    number = random.randint(1, 10)
    guess = None
    attempts = 0

    while guess != number:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            attempts += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
        except ValueError:
            print("Please enter a number.")

    print(f"Congratulations! You guessed it in {attempts} attempts.")

if __name__ == "__main__":
    play_game()

