import auction_logo
print(auction_logo.logo)
product = input("Enter the product name: ")
print(f"Welcome to the auction for {product}!")

def find_highest_bidder(bidding_dictonary):
  winner = ""
  highest_bid = 0 
  max(bidding_dictonary)
  for bidder in bidding_dictonary:
    bid_amount = bidding_dictonary[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The bid is goes to {winner} with a bid of amount is ${highest_bid}.") 
  
bids = {}
continue_bidding = True
while continue_bidding:
  name = input("Enter your name: ")
  price = int(input("Enter your bid amount: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
  if should_continue == "no":
    continue_bidding = False
    find_highest_bidder(bids)
  elif should_continue == "yes":
    print("\n" * 5) 