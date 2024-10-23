This script enables a user to define a biased coin and set the number of trials for flipping the coin. The result of this experiment is represented in a histogram saved as “coinToss.png”. In this example, the histogram depicts the outcome of 1000 tosses with a bias of 0.55 toward heads. 


As the number of flips, denoted by n, increases, we can start to notice an interesting pattern:  the probability of flipping a heads and the probability of flipping a tails begin to converge towards the user-defined probabilities. This convergence can be seen in the two line graphs “coinTossHeadsLineGraph.png” and “coinTossTailsLineGraph.png”. 
LMSR script
This script simulates a cost function based prediction market with two securities and two traders, governed by the Logarithmic Market Scoring Rule (LMSR). 

User defined actions: setting initial market state (quantities of Security 1 and Security 2), defining the market constant, placing a sequence of trades, closing the market, defining the outcome.

The script keeps track of both user states and the market state. The user state includes the quantity of shares each user owns for each security and the total amount the user has spent in the market. The market state includes the outstanding shares of each security. The program outputs data streams such as the cost of a trade, security prices, and total money spent in the market. At the market’s conclusion, trader compensations are revealed. 

The user can input trades to be executed on behalf of any of the traders in the market and they are prompted after each trade if they wish to close the market. As trades occur, security prices are updated based on the quantities bought or sold.

We can visually see the changes in price after each trade and how the degree of change depends on the value of b in “timeseriesPrices{market_constant}.png”.
