import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import numpy as np
import logging 

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


    headsFrequency = []
    tailsFrequency = []
    
    # Plotting a basic histogram
    output = bernoulli.rvs(headBias, size=coinTossTotal)

    # Create a line graph of frequencies
    headCounter= 0
    tailCounter = 0

    for count,x in enumerate(output):
        if x==1: 
            headCounter+=1
        else:
            tailCounter+=1
        headsFrequency.append(headCounter/(count+1))
        tailsFrequency.append(tailCounter/(count+1))
        
    headsArray = np.array(headsFrequency)
    tailsArray = np.array(tailsFrequency)
    theoreticalHeads = np.array([headBias] * coinTossTotal)
    theoreticalTails = np.array([1-headBias] * coinTossTotal)
    
    # Plot one: Relative frequencies using a bar chart
    plt.bar(['Tails', 'Heads'], [tailsFrequency[-1], headsFrequency[-1]], color='green', edgecolor='black')
    plt.xlabel('Outcome')
    plt.xticks([0,1], ['Tails', 'Heads'])
    plt.ylabel('Relative Frequency')
    plt.title(f'Coin Toss Simulation ({coinTossTotal} tosses, P(H) = {headBias})')
    plt.savefig(f'coinToss{coinTossTotal}_{headBias}.png') 
    plt.clf()

    # Plot two: Empirical Probability Over Time
    plt.title(f"Empirical Probability Over {coinTossTotal} tosses, P(H) = {headBias}")
    plt.plot(headsArray, color="blue", label='Heads')
    plt.plot(tailsArray, color="red", label='Tails')
    plt.plot(theoreticalHeads, color="black", linestyle=':',label=f"P(H)={headBias:.3f}")
    plt.plot(theoreticalTails, color="black", linestyle=':', label=f"P(T)={1-headBias:.3f}")
    plt.ylabel('Empirical Probability')
    plt.xlabel('Number of Flips')
    plt.ylim(0,1)
    plt.xlim(0,coinTossTotal)
    plt.legend()
    plt.savefig(f'coinTossLineGraph{coinTossTotal}_{headBias}.png')
    plt.clf()


if __name__ == "__main__":
    main()