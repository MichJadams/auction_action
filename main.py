from auctions.dutch_auction import dutch_auction
from auctions.penny_auction import penny_auction
from auctions.vickrey_auction import vickrey_auction

def initilize_players():
    number_of_players = int(input("How many players would like to submid a bid?\n"))
    players = []
    hotkeys = ["1", "2", "3"]
    for player in range(number_of_players):
        print("---------------------------------------------------")
        name = input(f"Player {player}, please input your name.\n")
        starting_cash = 10
        hotkey = hotkeys.pop(0) # TODO: add length check
        players.append({"name": name,
                        "hotkey": hotkey,
                        "starting_cash": starting_cash,
                        "current_cash": starting_cash,
                        "items": []})
        print(f"Welcome {name}! You have randomly been assigned a starting cash of {starting_cash}.")
        print(f"Your hotkey to press when bidding is {hotkey}.")

    return players


def main():
    players = initilize_players()
    still_playing = True
    while still_playing:
        print("Select which action you are interested in:")
        print("1. Dutch Auction")
        print("2. Vickrey Auction")
        print("3. Penny Auction")

        selection = int(input("press 1, 2 or 3 to select your auction type \n"))

        if selection == 1:
            players = dutch_auction(players)
        if selection == 2:
            players = vickrey_auction(players)
        if selection == 3:
            players = penny_auction(players)

        response = input("Do you wish to continue playing?(y/n) \n")
        if response != "y":
            still_playing = False

    print("Total winnings", players)


if __name__ == "__main__":
    main()
