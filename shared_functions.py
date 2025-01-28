import time
import random

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