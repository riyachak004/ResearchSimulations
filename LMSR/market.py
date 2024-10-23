import matplotlib.pyplot as plt
import numpy as np
import logging 
import math

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class MarketState: 
    def __init__(self, marketConstant, marketQuantity1, marketQuantity2):
        logger.info(f"Market Setup: Constant: {marketConstant}, Shares of Security 1: {marketQuantity1}, Shares of Security 2: {marketQuantity2}")
        logger.info("---------------------------------------------------------------")
        self.marketConstant = marketConstant
        self.marketQuantity1 = marketQuantity1
        self.marketQuantity2 = marketQuantity2
        self.eventOutcome = 0
    
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

userBook = {}

def updateUser(user: str="", quantity1:float=0, quantity2:float=0, cost:float=0):
    userBook[user].userQuantity1 += quantity1
    userBook[user].userQuantity2 += quantity2
    userBook[user].moneySpent += cost


def currentMarketCost(market: MarketState) -> float: 
    return market.marketConstant * np.log(pow(math.e, market.marketQuantity1/market.marketConstant) + pow(math.e, market.marketQuantity2/market.marketConstant))

def calculatePrice( market: MarketState, security:str="") -> float: 
    security1Component = pow(math.e, market.marketQuantity1/market.marketConstant)
    security2Component = pow(math.e, market.marketQuantity2/market.marketConstant)
    return security1Component/(security1Component + security2Component) if security == "Security1" else security2Component/(security1Component + security2Component)

def calculateCost(market: MarketState, quantity1:float=0, quantity2:float=0) -> float: 
    costPrior = currentMarketCost(market)
    market.marketQuantity1 += quantity1
    market.marketQuantity2 += quantity2
    costPost = currentMarketCost(market)
    return costPost - costPrior 

def calculateUserProfits(market: MarketState, userBook): 
    for key, user in userBook.items():
        logger.info(f"-----USER{user.userId} SUMMARY-----\n")
        logger.info(f"User{user.userId}, shares of Security 1: {user.userQuantity1}, Security 2: {user.userQuantity2}")
        if market.eventOutcome == 1: 
            revenue = user.userQuantity1
        else: 
            revenue = user.userQuantity2
        user.profit = revenue - user.moneySpent

        logger.info(f"Spent: {user.moneySpent}, Earned: {revenue}")
        logger.info(f"Net Profit: {user.profit}")

def main(): 
    logger.info("Simulation of LMSR Prediction Market - 2024 Presidental Election \nSecurity 1: Kamala Harris wins\nSecurity 2: Donald Trump wins\n")

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

    userBook["user1"] = User(userId=0)
    userBook["user2"] = User(userId=1)

    logger.info("--------BEGIN MARKET SIMULATION--------\n")

    tradeNumber = 0
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
        marketState = round(currentMarketCost(market), 3)

        updateUser(user, q1Update, q2Update, tradeCost)
        logger.info(f"Trade cost: {tradeCost}, Price of Security 1: {price1Update}, Price of Security 2: {price2Update}, Total spent in market: {marketState}")

        closeMarket = input("Would you like to terminate this market (Y/N)?")
        if closeMarket == "Y": 
            eventOutcome = input("Enter the event's outcome. Enter 1 if Harris wins the election and 2 if Trump wins: ")
            market.setEventOutcome(eventOutcome)
            break
        
        logger.info("-------------------NEW TRADE------------------\n")

    calculateUserProfits(market,userBook)


if __name__ == "__main__":
    main()