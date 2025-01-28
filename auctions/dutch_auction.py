from shared_functions import offer, get_item

explanation = """
In a dutch auction the auctioneer starts off with a
high price and then slowly lowers it until someone accepts the
price. So for this auction we
"""

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
