## Biased Coin Toss Script <br>
This script enables a user to define a biased coin and set the number of trials for flipping the coin. The result of this experiment is represented in a histogram saved as “coinToss{coinTossTotal}_{headBias}.png”. 

As the number of flips, denoted by n, increases, we can start to notice an interesting pattern: the probability of flipping a heads and the probability of flipping a tails begin to converge towards the user-defined probabilities. This convergence can be seen in the line graph “coinTossLineGraph{coinTossTotal}_{headBias}.png”. 

## Cost Function Based Prediction Market (LMSR) Script <br>
This script simulates a cost function based prediction market with two securities and two traders, governed by the Logarithmic Market Scoring Rule (LMSR). 

User defined actions: setting initial market state (quantities of Security 1 and Security 2), defining the market constant, placing a sequence of trades, closing the market, and defining the event outcome.

The script keeps track of both user states and the market state. The user state includes the quantity of shares each user owns for each security and the total amount the user has spent in the market. The market state includes the outstanding shares of each security. The program outputs the cost of a trade, security prices, and total money spent in the market after each trade. As trades occur, security prices are updated based on the quantities bought or sold. 
We can visually see the price changes after each trade and how the magnitude of these changes depends on the value of b in the file “timeseriesPrices{market_constant}.png”.

The user can input trades to be executed on behalf of any of the traders in the market, and after each trade, the user is asked if they wish to close the market. At the market’s conclusion, trader compensations are revealed. 
