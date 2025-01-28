from collections import defaultdict
from shared_functions import offer, get_item

explanation = """
In a penny auction, participants pay a non-refundable fee to place small
incremental bids (often one cent or a penny) on an item.
Each bid increases the item's price by a small amount and extends the auction time slightly.
The winner is the last bidder when the time runs out.
While the final price can be low, participants may spend
significant amounts on bidding fees.
"""

def penny_auction(players, items=["watch", "book", "chair"]):
    print(explanation)
    item = get_item(items)
    price = 1

    print(f"Current item: {item}, going for {price}")
    bidding_time_left_seconds = 10
    current_winner_name = "no initial bids"
    players_debts = defaultdict(int)

    while bidding_time_left_seconds > 0:
        print(f"time left: {bidding_time_left_seconds}")
        print(f"Current winner: {current_winner_name}")

        result = offer(1, players)
        while not result and bidding_time_left_seconds > 0:
            print(f"\t\t {bidding_time_left_seconds}: {current_winner_name}, {item} for {price}")
            bidding_time_left_seconds -= 1
            result = offer(1, players)

        if result:
            current_winner_name = result["name"]
            print(f"time extended by 5 seconds by {current_winner_name} for 1 cent")
            players_debts[current_winner_name] += 1
            price += 10
            bidding_time_left_seconds += 5
        else:
            break

# TODO: cover case where no bids placed
    print(f"The winner is {current_winner_name}, who won a {item} for {price}")
    items.remove(item)
    players_debts[current_winner_name] += price

    print("total debts")
    for player in players:
        if player["name"] in players_debts:
            player["current_cash"] -= players_debts[player["name"]]
            if player["name"] == current_winner_name:
                player["items"].append(item)
        print(f"{player["name"]} currently has {player["current_cash"]} and the following items")
        print(player["items"])
    return players
