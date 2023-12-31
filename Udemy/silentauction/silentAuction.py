
from art import logo

print(logo)
print("Welcome to the secret auction program.")
bidding_log = []


def bidding_phase(new_name, new_bid):
    new_bid = {
        "name": new_name,
        "bid": new_bid
    }
    bidding_log.append(new_bid)


def winner_phase(bidding):
    highest_bidder = 0
    winner_name = ""
    for check_bid in bidding:
        if check_bid["bid"] > highest_bidder:
            highest_bidder = check_bid["bid"]
            winner_name = check_bid["name"]
    return winner_name, highest_bidder


bidding = True
while bidding:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidding_phase(name, bid)
    new_bidder = ""
    while "yes" != new_bidder != "no":
        new_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if new_bidder == "no":
        bidding = False


winner, highest_bid = winner_phase(bidding_log)

print(f"{winner} won the auction with ${highest_bid}!")
