import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

nothing = '''
      _
     / )
    / /
   ( (  __   _
   (\ \( .> /_)
   (\\\ \ \_/ /
    \       /
     \    _/
     /   /
    /   /
   /   /
'''

#Write your code below this line 👇
options = [rock, paper, scissors, nothing]

computer = random.randint(0, 2)
# computer = 0

player = int(input("What do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if player > 3 or player < 0:
	player = 3
	
outcome = ""

if player == computer:
	outcome = "draw"
elif (player == 0 and computer == 2) or (player > computer and player < 2):
	outcome = "WOOHOO\nYOU WON"
else:
	outcome = "whomp whomp\nyou lose"
	
print(f"You chose: \n {options[player]}")
print(f"Computer chose:\n {options[computer]}")
print(outcome)