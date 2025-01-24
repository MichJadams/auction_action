

def main():
    print("Select which action you are interested in:")
    print("1. Dutch Auction")
    print("2. Vickrey Auction")
    print("3. Penny Auction")

    selection = input("press 1, 2 or 3 to select your auction type")

    if selection == 1:
        dutch_auction()
    if selection == 2:
        vickrey_auction()
    if selection == 3:
        penny_auction() 




if __name__ == "__main__":
    import doctest
    doctest.testmod()