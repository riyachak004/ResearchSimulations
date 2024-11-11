import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import numpy as np
import logging 
from biasNormalDis import biasNormalDis 
from biasBetaDis import biasBetaDis
from biasCoinGame import biasCoinGame

# source .venv/bin/activate
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def main():
    logger.info("Welcome to coin toss!")
    
    option = int(input("Visualize Normal Distribution: 0 \n Visualize Beta Distribution: 1\n Bias Coin Game: 2 \n What option would you like? "))
    
    if option == 0: 
        biasNormalDis()
    if option == 1: 
        biasBetaDis()
    if option == 2: 
        biasCoinGame()


if __name__ == "__main__":
    main()