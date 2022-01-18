# Silent Auction Program
# Made By Dean Mysliwiec
import os


# calculate the highest bidder
def calc_highest(a):
    # os.system('clr' if os.name == 'nt' else 'clear') //if ran on terminal
    print("\n" * 100) # when ran in pycharm
    highest_name = ""
    highest_bid = 0
    # check for the highest bid in the dictionary
    for key in a:
        if int(a[key]) > highest_bid:
            highest_bid = int(a[key])
            highest_name = key
    print(f"\n{highest_name} wins the auction with a bid of ${highest_bid}!")


# default dictionary
auction = {}

print("Welcome to the Silent Auction Program.")

# get user input
name = input("What is your name? ")
bid = input("What is your bid? $")

# add user data to the auction dictionary
auction[name] = bid

# ask if there are any other bidders
others = input("Are there any other bidders? Type 'yes' or 'no' : ").lower()

# if other bidders, continue on
while others != 'no':
    # os.system('clr' if os.name == 'nt' else 'clear') //if ran on terminal
    print("\n" * 100) # when ran in pycharm
    name = input("What is your name? ")
    bid = input("What is your bid? $")
    auction[name] = bid
    others = input("Are there any other bidders? Type 'yes' or 'no' : ").lower()

# calculate the highest bidder for the auction
calc_highest(auction)
