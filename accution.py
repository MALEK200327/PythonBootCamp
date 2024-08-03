import os
from accutionLogo import logo

auction = True
print(logo)
participant={}
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
while auction == True:
    print("Welcome to the auction!")
    Name= input("enter your name :\n")
    bid = int(input("Enter your bid:\n"))
    another_bider= input("is there another bid enter Y for Yes and N for No :\n")
    participant[Name] = bid
    if another_bider == "Y":
        os.system('clear')
        continue
    else:
        find_highest_bidder(participant)
        auction = False
    
        
