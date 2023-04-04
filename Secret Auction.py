#Import the clear() function from replit.
from replit import clear

#import & print logo
from art import logo
print(logo)

bids = {}
finished_bidding = False

#TODO 5 #Create a funcion to find the highest bidder.
def highest_bidder(records_of_bid):
  highest_bid = 0
  winner = ""
  for bidder in records_of_bid:
    bid_amount = records_of_bid[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
  
while not finished_bidding:
  #TODO 1 #Ask the user for their name.
  name = input("What is your name?: ")
  
  #TODO 2 #Ask the user for their bidding price.
  bid = int(input("What is your bid?: $"))
  
  #TODO 3 #Add name and bid to a dictionary.
  bids[name] = bid
  #TODO 4 #Ask the user if there are any other users who want to bid
  will_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if will_continue == "no":
    finished_bidding = True
    highest_bidder(bids)
  elif will_continue == 'yes':
    clear()