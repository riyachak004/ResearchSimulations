import matplotlib.pyplot as plt
import numpy as np
import logging 
import random

# source .venv/bin/activate
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def main():
    logger.info("Welcome to coin toss!")
    
    # Try catch block to ensure user entered bias and number of coin toss is a float and integer (respectively)
    try:
        headBias = float(input("Enter the bias of heads for your coin in decimal form (i.e. if you want P(flipping Heads) = 0.55, enter 0.55): "))
        coinTossTotal = int(input("How many coin tosses would you like simulated (i.e. 100): "))
        
        if headBias < 0 or headBias > 1:
            raise ValueError("Bias must be between 0 and 1")
        
    except ValueError as e:
        logger.error(f"Input error: {e}")
        return  # Gracefully exit

    headTotal = 0
    tailTotal = 0
    headsFrequency = []
    tailsFrequency = []

    # Flip the coin coinTossTotal many times and record results 
    for i in range(0,coinTossTotal):
        outcome = random.random()
        if outcome < headBias:
            headTotal+=1 
        else: 
            tailTotal+=1
        headsFrequency.append(float(headTotal/(i + 1)))
        tailsFrequency.append(float(tailTotal/(i + 1)))
    
    # Organize output 
    logger.info("Heads Total: %f", float(headTotal/coinTossTotal))
    logger.info("Tails Total: %f", float(tailTotal/coinTossTotal))
    data = ['Tails'] * tailTotal + ['Heads'] * headTotal
    
    # Plotting a basic histogram
    plt.hist(data, bins=2, color='green', edgecolor='black')
    
    # Adding labels and title
    plt.xlabel('Outcome')
    plt.ylabel('Frequency')
    plt.title(f'Coin Toss Simulation ({coinTossTotal} tosses, Bias: {headBias})')
    plt.savefig(f'coinToss{coinTossTotal}_{headBias}.png') 
    plt.clf()

    # Create a line graph of frequencies
    headsArray = np.array(headsFrequency)
    tailsArray = np.array(tailsFrequency)

    plt.title(f"Probability Over Time ({coinTossTotal} tosses, Bias: {headBias})")
    plt.plot(headsArray, color="blue", label='Heads')
    plt.plot(tailsArray, color="red", label='Tails')
    plt.ylabel('Probability')
    plt.xlabel('Number of Flips')
    plt.legend()
    plt.savefig(f'coinTossHeadsLineGraph{coinTossTotal}_{headBias}.png')
    plt.clf()


if __name__ == "__main__":
    main()