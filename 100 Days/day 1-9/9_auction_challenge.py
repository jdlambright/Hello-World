#from replit import clear
#HINT: You can call clear() to clear the output in the console.
#from art import logo


bids= {}
bidding_complete = False

def find_highest_bid(bidding_record):
  highest_bid= 0
  winner= ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid= bid_amount
      winner= bidder
      print(f"the winner is {winner} with a bid of ${highest_bid}")

while not bidding_complete:
  name = input("what is your name: ")
  price = int(input("what is your bid: $"))
  bids[name]= price
  more_bids= input("are there anymore bids? type yes or no: ")

  if more_bids== "no":
    bidding_complete=True
    find_highest_bid(bids)
  elif more_bids== "yes":
    clear()


