import robin_stocks.robinhood as r

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