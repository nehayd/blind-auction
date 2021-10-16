from replit import clear
from art import logo

auction = {}
def auction_function():
  print(logo)
  auctioner = str(input("What is your name?\n"))
  bid_price = input("Please state your bid price.\n")
  auction[auctioner] = bid_price
  other_users = input("Are there any other user who would like to bid? Type 'Yes' or 'No'\n")
  if other_users == "Yes":
    clear()
    auction_function()
  elif other_users == "No": 
    all_values = auction.values() 
    for name, bid in auction.items():
      if bid == max(all_values):
        print("%s is the winner" %name)

auction_function()

