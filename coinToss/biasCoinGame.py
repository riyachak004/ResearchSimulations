import random
import matplotlib.pyplot as plt
from scipy.stats import beta
import numpy as np
import logging 
import os

from scipy.stats import bernoulli

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def introBiasCoinGame(): 
    logger.info("Welcome to Bias Coin Game. We'll randomly select bias coin, but we will not unveil P(H) and P(T). Please decide whether "
                "you would like to continue playing the game at each iteration. Each iteration will be 10 flips and you will be "
                "shown the Beta distribution of the outcomes after each iteration.")
    

def continuePlaying(): 

    while True: 
        try:
            continue_playing = str(input("Continue Playing? Y/N: "))

            if continue_playing not in {'Y', 'N'}:
                raise ValueError("Invalid response")
            
            if continue_playing == 'Y': 
                return True
            else: 
                return False
            
        except ValueError as e:
            logger.error(f"Input error: {e}")
    

def biasCoinGame(): 
    introBiasCoinGame()

    headBias =  random.random() # randomly chose a coin bias
    print("headbias: ", headBias)
    alpha_value = 1
    beta_value = 1

    while continuePlaying(): 

        output = bernoulli.rvs(headBias, size=1000)

        alpha_value += sum(1 for x in output if x == 1)
        beta_value += sum(1 for x in output if x == 0)

        beta_dist = beta(alpha_value, beta_value)
        x = np.linspace(0, 1, 100)

        total = alpha_value + beta_value - 2

        relativeSucess = str((alpha_value-1)/total)
        relativeFailure = str((beta_value-1)/total)

        logger.info(f"Relative frequency of succeses: {relativeSucess}")
        logger.info(f"Relative frequency of failures: {relativeFailure}")
        logger.info(f"Total: {total}")
        
        # Generate the PDF of the beta distribution
        beta_pdf = beta_dist.pdf(x)
        plt.plot(x, beta_pdf)
        plt.xlabel('P(H)')
        plt.ylabel('Probability Density')
        plt.title(f'Bias Coin Game PDF of Beta Distribution, N={total} (α={alpha_value}, β={beta_value})')
        plt.legend()

        # Get the directory of the current script
        my_path = os.path.dirname(os.path.abspath(__file__))
        # Define the path for saving the plot in the 'visuals' folder
        imagePath = os.path.join(my_path, f'visuals/biasGame/N={total}_biasBetaDist_α={alpha_value}_β={beta_value}_pdf.png')

        plt.savefig(imagePath)
        plt.clf()
    
    logger.info(f"Bias revealed: {headBias}")
    



    
    
