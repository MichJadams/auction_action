from collections import defaultdict

explanation = """
Also known as a second-price sealed-bid auction,
participants submit written bids without knowing the bids of others.
The highest bidder wins, but the price paid is the second-highest bid.
This auction type encourages bidders to bid their true value,
as the winner pays less than their bid if they win.
"""
def vickrey_auction():
    print(explanation)

    number_of_players = int(input("How many players would like to submid a bid?"))
    item = "picture"
    bids = defaultdict(int)
    for player in range(number_of_players):
        bid = int(input(f"Player {player}, please input your bid for {item}"))
        bids[player] = bid
    
