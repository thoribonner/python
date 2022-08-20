import random
import os
from art import logo

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card(hand):
    '''Appends a random card from the deck to the hand provided.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    hand.append(random.choice(cards))

def calculate_score(cards):
    '''Takes a list of cards and returns the calculated score'''
    total = sum(cards)
    if total == 21 and len(cards) == 2:
        return 0
    if 11 in cards and total  > 21:
        cards.remove(11)
        cards.append(1)
        total = sum(cards)
    return total

def compare(player, computer):
    '''Accepts two scores and returns the result'''
    if player > 21 and computer > 21:
        return "You went over. You lose 😤"


    if player == computer:
        return "Draw 🫥"
    elif computer == 0:
        return "Lose, opponent has Blackjack 🤬"
    elif player == 0:
        return "Win with a Blackjack 😈"
    elif player > 21:
        return "You went over. You lose 🤬"
    elif computer > 21:
        return "Opponent went over. You win 😈"
    elif player > computer:
        return "You win 😈"
    else:
        return "You lose 🤬"
        

def play():
    print(logo)
    
    game_over = False

    player_hand = []
    computer_hand = []

    

    for _ in range(2):
        deal_card(player_hand)
        deal_card(computer_hand)

    while not game_over:

        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)

        print(f"\tYour cards: {player_hand}, current score: {player_score}")
        print(f"\tComputer's first card: {computer_hand[0]}")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            player_hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if player_hit == 'y':
                deal_card(player_hand)
            else:
                game_over = True
                
    while computer_score != 0 and computer_score < 17:
        deal_card(computer_hand)
        computer_score = calculate_score(computer_hand)

    print(f"\tYour final hand: {player_hand}, final score: {player_score}")
    print(f"\tComputer's final hand: {computer_hand}, final score: {computer_score}")
    print(compare(player_score, computer_score))

    
while input("Do you want to play a game of BlackJack?\n\tType 'y' or 'n': ") == 'y':
    clear()
    play()