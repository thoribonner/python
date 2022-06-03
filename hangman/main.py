import random
import os
from images import stages, logo
from words import word_list

def clear(): os.system('cls' if os.name == 'nt' else 'clear')
def cont(): os.system('python3 main.py')

clear()
print(logo)
print('\n')

gameover = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

guesses = []
hint = []
for _ in range(word_length):
    hint += "_"

print(f"{' '.join(hint)}\n")

while not gameover:
    guess = input("Guess a letter: ").lower()

    if len(guesses) > 4 and len(guesses) % 8 == 0:
        guesses += '\n'
    guesses += f"{guess}  "

    clear()



    if guess in hint:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            hint[position] = letter
    print(f"{' '.join(hint)}\n")
    print(f"letters you have tried:\n{''.join(guesses)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            gameover = True
            print("You lose.")
            print(f"the word was '{chosen_word}'.")
            
    
    if not "_" in hint:
        gameover = True
        print("\nYou win.")

    print(stages[lives])
    print(f"LIVES REMAINING: {lives}\n")

play_again = input("play again: 'y' or 'n'?\n")

if play_again == 'y' or play_again == 'yes' or play_again == 'yeah' or play_again == 'sure':
    cont()