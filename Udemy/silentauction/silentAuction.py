import os

from art import logo

print(logo)
print("Welcome to the secret auction program.")
bidding_log = []


def bidding_phase(name, bid):
    new_bid = {
        "name": name,
        "bid": bid
    }
    bidding_log.append(new_bid)


def winner_phase(bidding_log):
    highest_bid = 0
    winner = ""
    for check_bid in bidding_log:
        if check_bid["bid"] > highest_bid:
            highest_bid = check_bid["bid"]
            winner = check_bid["name"]
    return winner, highest_bid


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
