import os
from art import logo

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

welcome = "Welcome to our secret auction program."

print(logo)
print(welcome)

making_bids = True
bids = {}

def find_highest_bid(bid_record):
    winning_bid = 0
    winning_bidder = ""

    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > winning_bid:
            winning_bid = bid_amount
            winning_bidder = bidder
    print(f"The winner is {winning_bidder} with a bid of ${winning_bid}.")
    
while making_bids:
    name = input("What is your name?:  ")
    price = int(input("What is your bid?:  $"))
    continue_bidding = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    bids[name] = price

    if continue_bidding == 'yes':
        clear()
    else:
        making_bids = False
        find_highest_bid(bids)