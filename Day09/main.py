from replit import clear
from art import logo

auction_info = []
auction = True

def add_new_bidder(bidder_name, bidder_amount):
    new_bidder = {"name": bidder_name, "bid": bidder_amount}
    auction_info.append(new_bidder)

while auction:
    print(logo)
    print("Welcome to the private bidding auction")
    name = input("What is your name?: ").title()
    bid = float(input("How much would you like to bid?: $"))
    add_new_bidder(bidder_name=name, bidder_amount=bid)

    others = input("Are there any other bidders for this auction? Type 'yes' or 'no'.\n").lower()
    if others == 'no':
        auction = False
        highest_bidder = None
        for bidder in auction_info:
            if highest_bidder is None or bidder["bid"] > highest_bidder["bid"]:
                highest_bidder = bidder
        
        winner = highest_bidder["name"]
        highest_bid = highest_bidder["bid"]
        print(f"The highest bidder is {winner} with a bid of ${highest_bid:.2f}")
        print("Thank you for your participation.")
    else:
        clear()
