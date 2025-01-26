from auctions.dutch_auction import dutch_auction
from auctions.penny_auction import penny_auction
from auctions.vickrey_auction import vickrey_auction

def main():
    print("Select which action you are interested in:")
    print("1. Dutch Auction")
    print("2. Vickrey Auction")
    print("3. Penny Auction")

    selection = int(input("press 1, 2 or 3 to select your auction type\n"))
    total_winngins = {}
    print("you have selected", selection)
    if selection == 1:
        dutch_auction(total_winngins)
    if selection == 2:
        vickrey_auction()
    if selection == 3:
        penny_auction() 

    print("Total winnings", total_winngins)
    for item, winner in total_winngins.items():
        print(f"{winner["winner"]} won a {item} for only {winner["price"]}")


if __name__ == "__main__":
    main()