## Biased Coin Toss Script <br>
This script has three options. 

Option 1: Visualize Normal Distribution using a Biased Coin 
This option enables a user to define a biased coin and set the number of trials for flipping the coin. The result of this experiment is represented in a histogram saved as “coinToss{coinTossTotal}_{headBias}.png”. 

As the number of flips, denoted by n, increases, we can start to notice an interesting pattern: the probability of flipping a heads and the probability of flipping a tails begin to converge towards the user-defined probabilities. This convergence can be seen in the line graph “coinTossLineGraph{coinTossTotal}_{headBias}.png”. 

Option 2: Visualize Beta Distribution

Option 2.1: Generate One Graph Displaying Coin Toss Distribution
Chose option 1 when prompted. The user can visualize a beta distribution with respect to a coin toss. This option enables a user to enter 2 parameters that relate to a user's belief as to what the true probability of the biased coin is: alpha which corresponds to the number of successes and beta which corresponds to the number of failures. These two parameters generate the beta distribution. 

Option 2.2: Generate Many Graphs of Beta Distribution
Chose option 2 when prompted. 
The user can visualize the pdf's of a set of beta distributions, where alpha and beta are not constrainted to integer values. The values of alpha and beta are provided to the program in "biasBetaDis.py".

Option 3: Biased Coin Toss Game
The user can enter a bias coin probability or can let the system randomly chose. Then the user is prompted to provide an intial alpha and beta value. Once these parameters are chosen, the program will flip the biased coin 100 times and record the output. Alpha will be incremented by the number of heads flipped and beta will be incremented by the number of tails flipped. A graph of the updated alpha and beta values is produced. If the user choses to continue playing the game, another round will be played and the current alpha and beta values will be updated accordingly. 

## Biased Coin Toss Game <br>

## Cost Function Based Prediction Market (LMSR) Script <br>
This script simulates a cost function based prediction market with two securities and two traders, governed by the Logarithmic Market Scoring Rule (LMSR). 

User defined actions: setting initial market state (quantities of Security 1 and Security 2), defining the market constant, placing a sequence of trades, closing the market, and defining the event outcome.

The script keeps track of both user states and the market state. The user state includes the quantity of shares each user owns for each security and the total amount the user has spent in the market. The market state includes the outstanding shares of each security. The program outputs the cost of a trade, security prices, and total money spent in the market after each trade. As trades occur, security prices are updated based on the quantities bought or sold. 
We can visually see the price changes after each trade and how the magnitude of these changes depends on the value of b in the file “timeseriesPrices{market_constant}.png”.

The user can input trades to be executed on behalf of any of the traders in the market, and after each trade, the user is asked if they wish to close the market. At the market’s conclusion, trader compensations are revealed. 
