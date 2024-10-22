import matplotlib.pyplot as plt
import numpy as np
import logging 
import random

# source .venv/bin/activate
logger = logging.getLogger(__name__)

def main():
    print("Welcome to coin toss!")
    
    # Try catch block to ensure user entered bias and number of coin toss is a float and integer (respectively)
    try:
        headBias = float(input("Enter the bias of heads for your coin in decimal form (i.e. if you want P(flipping Heads) = 0.55, enter 0.55): "))
        coinTossTotal = int(input("How many coin tosses would you like simulated (i.e. 100): "))
        
        if headBias < 0 or headBias > 1:
            raise ValueError("Bias must be between 0 and 1")
        
    except ValueError as e:
        print(f"Input error: {e}")
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
            headsFrequency.append(float(headTotal/(i + 1)))
        else: 
            tailTotal+=1
            tailsFrequency.append(float(tailTotal/(i + 1)))
    
    # Organize output 
    print("Heads Total: ", float(headTotal/coinTossTotal))
    print("Tails Total: ", float(tailTotal/coinTossTotal))
    data = ['Tails'] * tailTotal + ['Heads'] * headTotal
    
    # Plotting a basic histogram
    plt.hist(data, bins=2, color='blue', edgecolor='black')
    
    # Adding labels and title
    plt.xlabel('Outcome')
    plt.ylabel('Frequency')
    plt.title(f'Coin Toss Simulation ({coinTossTotal} tosses, Bias: {headBias})')
    plt.savefig('coinToss.png') 
    plt.clf()

    # Create a line graph of frequencies
    headsArray = np.array(headsFrequency)

    plt.title("Heads Probability Over Time")
    plt.plot(headsArray)
    plt.ylabel('Probability')
    plt.xlabel('Number of Flips')
    plt.savefig('coinTossHeadsLineGraph.png')
    plt.clf()

    tailsArray = np.array(tailsFrequency)
    
    plt.title("Tails Probability Over Time")
    plt.plot(tailsArray)
    plt.ylabel('Probability')
    plt.xlabel('Number of Flips')
    plt.savefig('coinTossTailsLineGraph.png')


if __name__ == "__main__":
    main()