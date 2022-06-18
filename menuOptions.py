import spreads
import robin_stocks.robinhood.authentication as auth
#
#   The code below here is ONLY for the menu and navigation of RobinWave, please keep all behind the scenes code above this note...
#

def chooseBesslerSpreads():
    try:
        symbol = input("Enter Symbol: ").upper()
        topStrike = float(input("Enter TOP Strike: "))
        bottomStrike = float(input("Enter BOTTOM Strike: "))
        spreads.printBesslerSpreads(symbol, topStrike, bottomStrike)

        print("\nHit ENTER to start another Bessler Spread, or type 'menu' to go back to the menu...")
        whatNow = input("-> ").lower()
        if whatNow.startswith("m"):
            chooseMenu()
        else:
            chooseBesslerSpreads()
    except:
        print("\nSomething went wrong, please try again...\n")
        chooseBesslerSpreads()

def chooseCallSpreads():
    try:
        symbol = input("Enter Symbol: ").upper()
        calendarStrike = float(input("Enter Calendar Strike: "))
        spreads.printCallSpreads(symbol, calendarStrike)

        print("\nHit ENTER to start another Call Calendar Spread, or type 'menu' to go back to the menu...")
        whatNow = input("-> ").lower()
        if whatNow.startswith("m"):
            chooseMenu()
        else:
            chooseCallSpreads()
    except:
        print("\nSomething went wrong, please try again...\n")
        chooseCallSpreads()

def choosePutSpreads():
    try:
        symbol = input("Enter Symbol: ").upper()
        calendarStrike = float(input("Enter Calendar Strike: "))
        spreads.printPutSpreads(symbol, calendarStrike)

        print("\nHit ENTER to start another Call Calendar Spread, or type 'menu' to go back to the menu...")
        whatNow = input("-> ").lower()
        print(" ")
        if whatNow.startswith("m"):
            chooseMenu()
        else:
            choosePutSpreads()
    except:
        print("\nSomething went wrong, please try again...\n")
        chooseBesslerSpreads()

def logout():
    auth.logout()
    print("Logout Successful")


def chooseMenu():
    print("Welcome to Robin-Wave...\n")
    print("Current functionalities are as follows:")
    print("- Bessler Spreads ")
    print("- Call Calendar Spreads ")
    print("- Put Calendar Spreads ")
    print("- Logout ")
    print("\nPlease type: Bessler, Call, or Put to make your selection...")
    
    def menuOptions():
        whatNow = input("-> ").lower()
        if whatNow.startswith("b"):
            chooseBesslerSpreads()
        elif whatNow.startswith("c"):
            chooseCallSpreads()
        elif whatNow.startswith("p"):
            choosePutSpreads()
        elif whatNow.startswith("l"):
            logout()
        elif whatNow == 'end':
            x = input("Client is now broken... hit ENTER to close...")
        else:
            print("\nThat's not a valid input! Try Again...")
            menuOptions()
    menuOptions()