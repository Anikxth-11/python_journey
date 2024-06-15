import os
bidding_finished=False

BID={}


def highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount= bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f'THE WINNER OF THE BID IS {winner} WITH A BID OF {highest_bid} ')


while not bidding_finished:
    name=input('please enter your name:\n')
    bid_price=int(input("please enter the amount you want to bid:\n"))
    BID[name]=bid_price
    
    should_continue=input('is there any other bidder who wants to bid? type yes or no:\n')
    if should_continue =="no":
        bidding_finished = True
        highest_bidder(BID)
    elif should_continue =="yes":
        clear = lambda: os.system('cls')
        clear()
    
