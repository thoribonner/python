from art import logo, vs
from game_data import data
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_account():
    '''Get random account from data'''
    return random.choice(data)

def format(account):
    '''Returns string of account information'''
    n = account["name"]
    d = account["description"]
    c = account["country"]
    
    return f"{n}, a {d}, from {c}"

def check_answer(guess, a, b):
    '''compares followers and returns true if guess is correct'''
    if a > b:
        return guess == "a"
    else:
        return guess == "b"


def play_round():
    gameover = False
    score = 0
    optionA = choose_account()
    optionB = choose_account()

    
    while not gameover:
        while optionA["name"] == optionB["name"]:
            optionB = choose_account()
        print(logo)
        print(f"Compare A: {format(optionA)}")
        print(vs)
        print(f"Againt B: {format(optionB)}")
        af = optionA["follower_count"]
        bf = optionB["follower_count"]

        print(f"A = {af}, B = {bf}")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        is_correct = check_answer(guess, optionA["follower_count"], optionB["follower_count"])

        if is_correct:
            score += 1
            optionA = optionB
            optionB = choose_account()
            clear()
        else:
            gameover = True
            clear()
    print(f"Sorry, that's wrong. Final score: {score}\n\n\n")
    return
        

def game():
    play_on = True
    while play_on:
        play_round()
        play_on = input("Would you like to play again? Type 'y' or 'n': ") == 'y'
    clear()
    print("Thanks for playing!")
    
game()