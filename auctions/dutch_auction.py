import time
import msvcrt
import random

explanation = """
In a dutch auction the auctioneer starts off with a
high price and then slowly lowers it until someone accepts the
price. So for this auction we
"""


def get_item(options):
    return random.choice(options) if len(options) > 0 else ""


def get_player_key(pressed_key, players):
    for player in players:
        if player["hotkey"] == pressed_key:
            return player
    return False


def offer(duration, players):
    """
    This function will wait for the given duration expecting a key press
    If no keypress comes it returns false 
    I didn't use python's "Input()" function because I think that waits forever for input
    """

    start_time = time.time()
    while time.time() - start_time < duration:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8')
            player = get_player_key(key, players)
            if player:
                print(f"detected bid from {player["name"]}")
                return player
            else:
                print(f"invalid key press, could not find player with hotkey {key}")
                print("bidding is still open")
    return False

def dutch_auction(players, items=["watch", "book", "chair"]):
    print(explanation)

    item_value: int = 45
    round_number: int = 1
    item = get_item(items)
    if item == "":
        print("ooops, we have bought all the items in the warehouse...")
        return

    input("when you are ready, hit enter")
    while item_value > 0:
        print("-----------------------Starting round------------------\n", round_number)
        print(f"a beautiful {item} going for {item_value}.")
        for time_number in ["once", "twice", "three times"]:
            print(f"going {time_number}")
            winner = offer(10, players)
            if winner:
                print(f"sold to participent number {winner["name"]} for {item_value}")
                winner["current_cash"] -= item_value
                winner["items"].append({"price": item_value, "name": item})
                items.remove(item)
                return players

        item_value -= 5
    return players
