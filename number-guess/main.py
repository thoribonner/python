import random
from art import title

EASY_LIVES = 10
HARD_LIVES = 5

# function to accept and return player guess
def make_guess():
    '''returns input as number'''
    return int(input("Make a guess: "))

# function to check player guess to actual number
def compare(actual, guessed, lives_remaining):
    '''compares actual number to player guess returns lives remaining'''
    if actual > guessed:
        print("Too low. 📉")
        return lives_remaining - 1
    if actual < guessed:
        print("Too high. 📈")
        return lives_remaining - 1
    else:
        print(f"You got it! The number was {actual}.")
def set_difficulty():
    difficulty = input("Choose a difficulty:\n\tType 'easy' or 'hard':\t").lower()
    if difficulty == 'easy':
        return EASY_LIVES
    else:
        return HARD_LIVES

def play():
    number = random.randint(1, 100)
    
    print(title)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    lives = set_difficulty();

    guess = 0

    while guess != number:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = make_guess()
        lives = compare(number, guess, lives)

        if lives == 0:
            print(f"Womp, womp.\nThe number was {number}.\nYou didn't guess correctly. 👻")
            return
        elif guess != number:
            print("Guess again! 🫣")
        

play()