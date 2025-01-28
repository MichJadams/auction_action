from shared_functions import get_item
explanation = """
Also known as a second-price sealed-bid auction,
participants submit written bids without knowing the bids of others.
The highest bidder wins, but the price paid is the second-highest bid.
This auction type encourages bidders to bid their true value,
as the winner pays less than their bid if they win.
"""

def vickrey_auction(players, items=["watch", "book", "chair"]):
    print(explanation)

    item = get_item(items)
    bids = []
    print("private biding has begun")
    for player in players:
        print("------------------------------------------------")
        bid = int(input(f"Player {player["name"]}, please input your bid for a {item}\n"))
        bids.append({"player": player, "bid": bid})
    bids.sort(key=sort_by_bid)
    winner = bids[-1]
    second = bids[-2]
    for player in players:
        if player["name"] == winner["player"]["name"]:
            player["items"].append(item)
            player["current_cash"] -= second["bid"]
    print(f"The winner is {winner["player"]["name"]} and while they bid {winner["bid"]} they will only have to pay the price of the second highest bidder, {second["player"]["name"]} who bid {second["bid"]}")

    return

def sort_by_bid(bid):
    return bid["bid"]

