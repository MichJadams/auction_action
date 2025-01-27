import time
import msvcrt
from collections import defaultdict

"""
**Penny Auction**:
- In a penny auction, participants pay a non-refundable fee to place small
incremental bids (often one cent or a penny) on an item.
Each bid increases the item's price by a small amount and extends the auction time slightly.
The winner is the last bidder when the time runs out.
While the final price can be low, participants may spend
significant amounts on bidding fees.

"""
explanation = ""


def offer(duration):
    """
    This function will wait for the given duration expecting a key press
    If no keypress comes it returns false
    I didn't use python's "Input()" function because I think that waits forever for input
    """
    start_time = time.time()
    while time.time() - start_time < duration:
        key = msvcrt.kbhit()
        if key:
            return key
    return False


def penny_auction(players, items=["watch", "book", "chair"]):
    print(explanation)
    item = "throne"
    price = 1
    print(f"Current item: {item}, going for {price}")
    bidding_time_left_seconds = 10
    current_winner = "no initial bids"
    players_debts = defaultdict(int)
    while bidding_time_left_seconds > 0:
        print(f"time left: {bidding_time_left_seconds}")
        print(f"Current winner: {current_winner}")

        result = offer(1)
        while not result and bidding_time_left_seconds > 0:
            print(f"\t\t {bidding_time_left_seconds}: {current_winner}")
            bidding_time_left_seconds -= 1
            result = offer(1)

        if result:
            current_winner = result.decode('utf-8')
            print(f"time extended by 5 seconds by {current_winner} for 1 cent")
            players_debts[current_winner] += 1
            price += 10
            bidding_time_left_seconds += 5
        else:
            break

    print(f"The winner is {current_winner}, who won a {item} for {price}")
    players_debts[current_winner] += price
    print("total debts")
    for player in players_debts:
        print(f"{player} owes {players_debts[player]} because they bid {players_debts[player]} times")
    return
