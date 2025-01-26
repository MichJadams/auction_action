import time
import msvcrt
import random

explanation = """
In a dutch auction the auctioneer starts off with a
high price and then slowly lowers it until someone accepts the
price. So for this auction we
"""


def get_item(total_winnings):
    options = [x for x in ["watch", "book", "chair"] if x not in total_winnings]
    return random.choice(options) if len(options) > 0 else False


def offer(duration=10):
    """
    This function will wait for the given duration expecting a key press
    If no keypress comes it returns false 
    I didn't use python's "Input()" function because I think that waits forever for input
    """
    start_time = time.time()
    while time.time() - start_time < duration:
        if msvcrt.kbhit():
            return msvcrt.getch()
    return False


def dutch_auction(total_winnings=None):
    if total_winnings is None:
        total_winnings = {}
    print(explanation)
    print("At any time you may press the number on the keyboard that represents you to place a bit.")
    print(
        "e.g. player 2 dcides that they see a bit they are interested in, they press 2 as soon as it comes up on the screen.")
    item_value: int = 45
    round_number: int = 1
    item = get_item(total_winnings)
    if not item:
        print("ooops")
        return

    while item_value > 0:
        print("-----------------------Starting round------------------", round_number)
        print(f"a beautiful {item} going for {item_value}.")
        for time_number in ["once", "twice", "three times"]:
            print(f"going {time_number}")
            result = offer(10)
            if result:
                print(f"sold to participent number {result.decode('utf-8')}")
                total_winnings[item] = {"price": item_value, "winner": result.decode('utf-8')}
                if play_again():
                    return dutch_auction(total_winnings)
                else:
                    return total_winnings

        item_value -= 5


def play_again():
    response = input("Would you like to play this same auction again?(Y/N)")
    if response == "y":
        return True
    else:
        return False
