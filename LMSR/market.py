import matplotlib.pyplot as plt
import numpy as np
import logging 
import math

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class MarketState: 
    def __init__(self, marketConstant, marketQuantity1, marketQuantity2):
        logger.info(f"Market Setup: Constant: {marketConstant}, Shares of Security 1: {marketQuantity1}, Shares of Security 2: {marketQuantity2}")
        logger.info("-------------------------------------------------------------------------")
        self.marketConstant = marketConstant
        self.marketQuantity1 = marketQuantity1
        self.marketQuantity2 = marketQuantity2
        self.eventOutcome = 0
        self.aggregateMarketCost = 0
    
    def setEventOutcome(self, eventOutcome:str):
        try: 
            self.eventOutcome = int(eventOutcome)
            if self.eventOutcome != 1 and self.eventOutcome != 2:
                raise ValueError("Invalid outcome value. Use 1 for Security 1 and 2 for Security 2.")
                
        except ValueError as e:
            logger.error(f"Invalid Event Outcome: {e}")
            return 

class User: 
    def __init__(self, userId): 
        self.userId = int(userId)
        self.userQuantity1 = 0
        self.userQuantity2 = 0
        self.moneySpent = 0
        self.profit = 0

# Set of traders
userBook = {}
security1Prices = []
security2Prices = []

def updateUser(user: str="", quantity1:float=0, quantity2:float=0, cost:float=0):
    """Adjusts the user's security quantities following a trade."""
    userBook[user].userQuantity1 += quantity1
    userBook[user].userQuantity2 += quantity2
    userBook[user].moneySpent += cost


def currentMarketCost(market: MarketState) -> float: 
    """Calculates the current cost of the market using LMSR's Cost Function."""
    return market.marketConstant * np.log(pow(math.e, market.marketQuantity1/market.marketConstant) + pow(math.e, market.marketQuantity2/market.marketConstant))

def aggregateMarketCost(market: MarketState) -> float: 
    """Returns the total amount of money traders have spent in the market."""
    return market.aggregateMarketCost

def calculatePrice( market: MarketState, security:str="") -> float: 
    """Returns the current market price of the security."""
    security1Component = pow(math.e, market.marketQuantity1/market.marketConstant)
    security2Component = pow(math.e, market.marketQuantity2/market.marketConstant)
    return security1Component/(security1Component + security2Component) if security == "Security1" else security2Component/(security1Component + security2Component)

def calculateCost(market: MarketState, quantity1:float=0, quantity2:float=0) -> float: 
    """Calculates the cost of trade."""
    costPrior = currentMarketCost(market)
    market.marketQuantity1 += quantity1
    market.marketQuantity2 += quantity2
    costPost = currentMarketCost(market)
    totalCost = costPost - costPrior 
    market.aggregateMarketCost+=totalCost
    return totalCost

def calculateUserProfits(market: MarketState, userBook): 
    """Determines the net compensation of each trader based on the event's outcome """
    for key, user in userBook.items():
        logger.info(f"user{user.userId}, shares of Security 1: {user.userQuantity1}, Security 2: {user.userQuantity2}")
        if market.eventOutcome == 1: 
            revenue = user.userQuantity1
        else: 
            revenue = user.userQuantity2
        user.profit = revenue - user.moneySpent

        logger.info(f"Spent: {user.moneySpent}, Earned: {revenue}")
        logger.info(f"Net Profit: {user.profit}\n")
    
def produceTimeSeries(market: MarketState): 
    n = len(security1Prices)
    security1Timeseries = np.array(security1Prices)
    security2Timeseries = np.array(security2Prices)

    plt.title("Timeseries of Security Prices")
    plt.plot(security1Timeseries, color="blue", label='Security 1')
    plt.plot(security2Timeseries, color="red", label='Security 2')
    plt.ylabel('Price')
    plt.xticks(np.arange(0, n, 1))
    plt.ylim(0, 1)
    plt.xlabel('Trade Number')
    plt.legend()
    plt.savefig(f'timeseriesPrices{market.marketConstant}.png')
    plt.clf()

def main(): 
    logger.info("Simulation of LMSR Prediction Market - 2024 Presidental Election \nSecurity 1: Kamala Harris wins\nSecurity 2: Donald Trump wins\n")

    # Requests user input for intial market setup
    try:
        marketQuantity1 = float(input("Input outstanding shares of Security 1: "))
        marketQuantity2 = float(input("Input outstanding shares of Security 2: "))
        inputMarketConstant = float(input("Input market constant: "))

        if inputMarketConstant <= 0: 
            logger.error(f"Input error: market constant must be greater than 0")
            return

        market = MarketState(inputMarketConstant, marketQuantity1, marketQuantity2)

    except ValueError as e:
        logger.error(f"Input error: {e}")
        return  # Gracefully exit

    logger.info("Users are: user1, user2 \nInput a trade as follows: user, Security 1 shares, Security 2 shares\n")

    userBook["user1"] = User(userId=1)
    userBook["user2"] = User(userId=2)
    tradeNumber = 0

    intialPrice1 = round(calculatePrice(market, "Security1"), 3)
    intialPrice2 = round(calculatePrice(market, "Security2"), 3)
    security1Prices.append(intialPrice1)
    security2Prices.append(intialPrice2)

    logger.info("--------BEGIN MARKET SIMULATION--------\n")

    # Market Open - trades are executed until market closes
    while True: 
        trade = input(f"Execute Trade {tradeNumber}: ")
        
        try: 
            user, q1Update, q2Update = trade.split(",")
            q1Update = float(q1Update)
            q2Update = float(q2Update)
            if user not in userBook: 
                logger.error("User not in user book")
                raise ValueError

        except ValueError as e:
            logger.error("Invalid trade format. Please follow 'user, Security 1 shares, Security 2 shares'")
            continue
       
        tradeNumber+=1
        tradeCost = round(calculateCost(market, q1Update, q2Update), 3)
        price1Update = round(calculatePrice(market, "Security1"), 3)
        price2Update = round(calculatePrice(market, "Security2"), 3)
        security1Prices.append(price1Update)
        security2Prices.append(price2Update)
        marketState = round(aggregateMarketCost(market), 3)

        updateUser(user, q1Update, q2Update, tradeCost)
        logger.info(f"Trade cost: {tradeCost}, Price of Security 1: {price1Update}, Price of Security 2: {price2Update}, Total spent in market: {marketState}")

        closeMarket = input("Would you like to terminate this market (Y/N)?")
        if closeMarket == "Y": 
            # User has decided to terminate market
            eventOutcome = input("Enter the event's outcome. Enter 1 if Harris wins the election and 2 if Trump wins: ")
            market.setEventOutcome(eventOutcome)
            break
        
        logger.info("-------------------------------------NEW TRADE------------------------------------\n")

    calculateUserProfits(market,userBook)
    produceTimeSeries(market)

if __name__ == "__main__":
    main()