import time
import msvcrt
import random

explanation = """
In a dutch auction the auctioneer starts off with a
high price and then slowly lowers it until someone accepts the
price. So for this auction we
"""


def get_item(options):
    return random.choice(options) if len(options) > 0 else False


def offer(duration, valid_keys):
    """
    This function will wait for the given duration expecting a key press
    If no keypress comes it returns false 
    I didn't use python's "Input()" function because I think that waits forever for input
    """
    start_time = time.time()
    while time.time() - start_time < duration:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8')
            if key in valid_keys:
                print(f"detected bid from {key}")
                return key
            else:
                print(f"invalid key press, could not find player {key}")
                print("bidding is still open")
    return False

def assign_keys_to_players(players):
    print("I will now assign numbers on the keyboard to players")
    key_to_player = {}

    for key, player in enumerate(players):
        print(f"{player["name"]} you have number {key + 1}")
        key_to_player[str(key + 1)] = player
    print(
            "At any time you may press the number on the keyboard that has been assigned to you time will be added to the clock and you will have placed a bid at the current item value.")
    print("e.g. player 2 decides that they see a bit they are interested in, they press 2 as soon as it comes up on the screen.")
    return key_to_player
def dutch_auction(players, items=["watch", "book", "chair"]):
    print(explanation)

    key_to_player = assign_keys_to_players(players)


    item_value: int = 45
    round_number: int = 1
    item = get_item(items)
    if not item:
        print("ooops, we have bought all the items in the warehouse...")
        return

    input("when you are ready, hit enter")
    while item_value > 0:
        print("-----------------------Starting round------------------\n", round_number)
        print(f"a beautiful {item} going for {item_value}.")
        for time_number in ["once", "twice", "three times"]:
            print(f"going {time_number}")
            bid_key_press = offer(10,key_to_player.keys())
            if bid_key_press:
                winner = key_to_player[bid_key_press]
                print(f"sold to participent number {winner["name"]} for {item_value}")
                winner["current_cash"] -= item_value
                winner["items"].append({"price": item_value, "name": item})

                return [player for key, player in key_to_player.items()]

        item_value -= 5
