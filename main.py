import robin_stocks

r = robin_stocks.robinhood

# trys to open the Account.txt file with username and password and then grabs them and puts them in the designated variables.
try:
    with open("Account.txt", "r") as accountFile:
        username = accountFile.readline().rstrip("\n").strip("Username: ").strip()
        password = accountFile.readline().rstrip("\n").strip("Password: ").strip()
except:
    with open("Account.txt", "w+") as accountFile:
        infoCheck = False
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        while not infoCheck:
            print("\nIs This Information Correct?")
            print("Username: "+str(username))
            print("Password: "+str(password))
            userAnswer = input("Yes Or No ---> ")

            if userAnswer.startswith('y') or userAnswer.startswith('Y'):
                accountFile.write("Username: "+str(username)+"\n")
                accountFile.write("Password: "+str(password)+"\n")
                infoCheck = True
            else:
                infoCheck = False
                username = input("Re-Enter Username: ").strip()
                password = input("Re-Enter Password: ").strip()


print("\n= Currently Trying To Login as: '"+str(username)+"'")


# Variables For Loggin In...
username = None
password = None
expiresIn = 8640000
scope = 'internal'
by_sms = True
store_session = True
mfa_code = None

# Logs into your robinhood account using just your username and your password.
login_response = r.authentication.login(username, password, expiresIn, scope, by_sms, store_session, mfa_code)
accessToken = str(login_response["token_type"])


# This Will Show the Current Account Balance
def accountBalance():
    totalBalance = round(float(r.profiles.load_portfolio_profile(info='equity')),2)
    return totalBalance
print("\n= Account Balance: ${:,.2f} \n".format(accountBalance()))


# Variables for Robinhood API 'find_options_by_expiration_and_strike()'
expirationDate = None
strikePrice = None
optionType = None
info = None
typeCall = 'call'
typePut = 'put'



def printBesslerSpreads(symbol, topStrike, bottomStrike):
    count = 0
    stockPrice = "$"+str(round(float(r.stocks.get_quotes(symbol, info='last_trade_price')[0]), 2))
    optionDates = r.options.get_chains(symbol, info=None)['expiration_dates']
    spreadCount = len(optionDates)-1
    print("\n\n--------- Strike: $"+str(round(topStrike))+" ---------")
    print("--------- Strike: $"+str(round(bottomStrike))+" ---------")
    print("---  '"+symbol+"' Current: "+stockPrice+"  ---\n")
    print("Sell Date     Buy Date     Cost")
    for i in range(spreadCount):
        try:
            expDate1 = optionDates[count]
            expDate2 = optionDates[count+1]

            callSellPrice = float(r.options.find_options_by_expiration_and_strike(inputSymbols=symbol, expirationDate=expDate1, strikePrice=topStrike, optionType=typeCall, info='adjusted_mark_price')[0])
            callBuyPrice =  float(r.options.find_options_by_expiration_and_strike(inputSymbols=symbol, expirationDate=expDate2, strikePrice=topStrike, optionType=typeCall, info='adjusted_mark_price')[0])
            putSellPrice =  float(r.options.find_options_by_expiration_and_strike(inputSymbols=symbol, expirationDate=expDate1, strikePrice=bottomStrike, optionType=typePut, info='adjusted_mark_price')[0])
            putBuyPrice =   float(r.options.find_options_by_expiration_and_strike(inputSymbols=symbol, expirationDate=expDate2, strikePrice=bottomStrike, optionType=typePut, info='adjusted_mark_price')[0])
            
            count += 1
            print(str(expDate1)+" - "+str(expDate2)+"   $"+str(round(((callBuyPrice+putBuyPrice)-(callSellPrice+putSellPrice))*100,2)))
        except:
            print("Error loading data for this week...")
    print(" ")


def printCallSpreads(symbol, calendarStrike):
    count = 0
    stockPrice = "$"+str(round(float(r.stocks.get_quotes(symbol, info='last_trade_price')[0]), 2))
    optionDates = r.options.get_chains(symbol, info=None)['expiration_dates']
    spreadCount = len(optionDates)-1
    print("\n\n--------- Strike: $"+str(round(calendarStrike))+" ---------")
    print("---  '"+symbol+"' Current: "+stockPrice+"  ---\n")
    print("Sell Date     Buy Date     Cost")
    for i in range(spreadCount):
        try:
            expDate1 = optionDates[count]
            expDate2 = optionDates[count+1]

            callSellPrice = float(r.options.find_options_by_expiration_and_strike(inputSymbols=symbol, expirationDate=expDate1, strikePrice=calendarStrike, optionType=typeCall, info='adjusted_mark_price')[0])
            callBuyPrice =  float(r.options.find_options_by_expiration_and_strike(inputSymbols=symbol, expirationDate=expDate2, strikePrice=calendarStrike, optionType=typeCall, info='adjusted_mark_price')[0])
            
            count += 1
            print(str(expDate1)+" - "+str(expDate2)+"   $"+str(round((callBuyPrice-callSellPrice)*100,2)))
        except:
            print("Error loading data for this week...")
    print(" ")


def printPutSpreads(symbol, calendarStrike):
    count = 0
    stockPrice = "$"+str(round(float(r.stocks.get_quotes(symbol, info='last_trade_price')[0]), 2))
    optionDates = r.options.get_chains(symbol, info=None)['expiration_dates']
    spreadCount = len(optionDates)-1
    print("\n\n--------- Strike: $"+str(round(calendarStrike))+" ---------")
    print("---  '"+symbol+"' Current: "+stockPrice+"  ---\n")
    print("Sell Date     Buy Date     Cost")
    for i in range(spreadCount):
        try:
            expDate1 = optionDates[count]
            expDate2 = optionDates[count+1]

            putSellPrice =  float(r.options.find_options_by_expiration_and_strike(inputSymbols=symbol, expirationDate=expDate1, strikePrice=calendarStrike, optionType=typePut, info='adjusted_mark_price')[0])
            putBuyPrice =   float(r.options.find_options_by_expiration_and_strike(inputSymbols=symbol, expirationDate=expDate2, strikePrice=calendarStrike, optionType=typePut, info='adjusted_mark_price')[0])
            
            count += 1
            print(str(expDate1)+" - "+str(expDate2)+"   $"+str(round((putBuyPrice-putSellPrice)*100,2)))
        except:
            print("Error loading data for this week...")
    print(" ")








#
#   The code below here is ONLY for the menu and navigation of RobinWave, please keep all behind the scenes code above this note...
#

def chooseBesslerSpreads():
    try:
        symbol = input("Enter Symbol: ").upper()
        topStrike = float(input("Enter TOP Strike: "))
        bottomStrike = float(input("Enter BOTTOM Strike: "))
        printBesslerSpreads(symbol, topStrike, bottomStrike)

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
        printCallSpreads(symbol, calendarStrike)

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
        printPutSpreads(symbol, calendarStrike)

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


def chooseMenu():
    print("Welcome to Robin-Wave...\n")
    print("Current functionalities are as follows:")
    print("- Bessler Spreads ")
    print("- Call Calendar Spreads ")
    print("- Put Calendar Spreads ")
    print("\nPlease type: Bessler, Call, or Put to make your selection...")
    
    def menuOptions():
        whatNow = input("-> ").lower()
        if whatNow.startswith("b"):
            chooseBesslerSpreads()
        elif whatNow.startswith("c"):
            chooseCallSpreads()
        elif whatNow.startswith("p"):
            choosePutSpreads()
        elif whatNow == 'end':
            x = input("Client is now broken... hit ENTER to close...")
        else:
            print("\nThat's not a valid input! Try Again...")
            menuOptions()
    menuOptions()
    
chooseMenu()











