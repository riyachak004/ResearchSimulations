import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import numpy as np
import logging 
from biasNormalDis import biasNormalDis 
from biasBetaDis import biasBetaDis

# source .venv/bin/activate
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def main():
    logger.info("Welcome to coin toss!")
    
    distribution = int(input("Normal Distribution: 0 \nBeta Distribution: 1\nWhat distribution would you like? "))
    
    if distribution == 0: 
        biasNormalDis()
    if distribution == 1: 
        biasBetaDis()

if __name__ == "__main__":
    main()