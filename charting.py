import robin_stocks.robinhood as r
import matplotlib.pyplot as plt



# Universal Option

def chartTest():
    symbol = 'TSLA'
    strikePrice = 1130
    optionType = 'call'
    interval = '5minute'
    span = 'week'
    bounds = 'regular'
    info = 'low_price'

    expirationDate = '2021-11-05'
    sellPointList = []
    sellResult = r.get_option_historicals(symbol, expirationDate, strikePrice, optionType, interval, span, bounds, info)
    for price in sellResult:
        sellPointList.append(float(price))

    expirationDate = '2021-11-12'
    buyPointList = []
    buyResult = r.get_option_historicals(symbol, expirationDate, strikePrice, optionType, interval, span, bounds, info)
    for price in buyResult:
        buyPointList.append(float(price))

    def combineSellBuy(sellPointList, buyPointList):
        count = 0
        finalPointList = []
        for point in sellPointList:
            sell = point
            buy = buyPointList[count]
            finalPointList.append(buy-sell)
        return finalPointList

    print(len(sellPointList))
    print(len(buyPointList))

    prices = combineSellBuy(sellPointList, buyPointList)
    plt.plot(prices)
    plt.ylabel("cost per")
    plt.show()

 

# sell,tna,call,2021-11-05: 91,93,96,99
def getFilteredOptionsPrices(commandString):
    interval = '5minute'
    span = 'week'
    bounds = 'regular'
    info = 'close_price'

    command = commandString.split(":")
    filter = command[0].strip(" ").split(",")
    strikesString = command[1].strip(" ").split(",")
    strikes = [float(x) for x in strikesString]

    action = filter[0].lower()
    symbol = filter[1].upper()
    optionType = filter[2].lower()
    expirationDate = filter[3]

    setsOfPrices = []
    for count in range(0,len(strikes)):
        strikePrice = strikes[count]
        priceList = r.get_option_historicals(symbol, expirationDate, strikePrice, optionType, interval, span, bounds, info)
        priceList = [float(x) for x in priceList]
        setsOfPrices.append(priceList)

    listLength = len(setsOfPrices[0])
    itemCount = 0
    masterList = []
    for i in range(listLength):
        masterList.append(0)
        itemCount += 1
    setsOfPrices.insert(0,masterList)
    return setsOfPrices


    








