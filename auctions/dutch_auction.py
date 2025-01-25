
import time
import msvcrt

explanation = """
In a dutch auction the auctioneer starts off with a
high price and then slowly lowers it until someone accepts the
price. So for this auction we
"""
def offer(duration = 10):
    """
    This function will wait for the given duration expecting a key press
    If no keypress comes it returns false 
    I didn't use python's "Input()" function because I think that waits forever for input
    """
    start_time = time.time()
    while time.time() - start_time < duration:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            return key
    return False
def dutch_auction():
    print(explanation)
    # print("Please enter how many participents are playing.")
    # participents: int = int(input("(max is 9):"))
    print("At any time you may press the number on the keyboard that represents you to place a bit.")
    print("e.g. player 2 dcides that they see a bit they are interested in, they press 2 as soon as it comes up on the screen.")

    item_value: int = 45
    round_number: int = 1
    item = "clock"
    times = ["once", "twice", "three times"]
    while item_value > 0:
        print("Starting round ", round_number)
        print(f"a beautiful {item} going for {item_value}.")
        for time_number in times:
            print(f"going {time_number}")
            result = offer(10)
            if result:
                print(f"sold to participent number {result.decode('utf-8')}")
                return


        print("no bids, moving on!")
        item_value -= 5
