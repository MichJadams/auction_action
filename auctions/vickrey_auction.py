from collections import defaultdict

explanation = """
Also known as a second-price sealed-bid auction,
participants submit written bids without knowing the bids of others.
The highest bidder wins, but the price paid is the second-highest bid.
This auction type encourages bidders to bid their true value,
as the winner pays less than their bid if they win.
"""
def vickrey_auction(players, items=["watch", "book", "chair"]):
    print(explanation)

    item = "picture"
    bids = []
    print("private biding has begun")
    for player in range(number_of_players):
        print("------------------------------------------------")
        bid = int(input(f"Player {name}, please input your bid for a {item}\n"))
        bids.append({"player": name, "bid": bid})
    bids.sort(key=sort_by_bid)
    winner = bids[-1]
    second = bids[-2]
    
    print(f"The winner is {winner["player"]} and while they bid {winner["bid"]} they will only have to pay the price of the second highest bidder, {second["player"]} who bid {second["bid"]}")

    return

def sort_by_bid(bid):
    return bid["bid"]

