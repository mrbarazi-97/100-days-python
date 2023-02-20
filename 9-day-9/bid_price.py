import os
print("Logo is here")
def clear(): return os.system('clear')


bids = {}
bidding_finished = False


def find_highest_bid(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with ${bid_amount}")


while not bidding_finished:
    name = input("Please enter your name : ")
    price = int(input("Please enter bid price : "))
    bids[name] = price
    should_continue = input("Do you want to add new person ? 'yes' or 'no' \n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bid(bids)
    elif should_continue == "yes":
        clear()  # clear the console screen
