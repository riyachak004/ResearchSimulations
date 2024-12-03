import matplotlib.pyplot as plt
from scipy.stats import beta
import numpy as np
import logging 
import os

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def biasBetaDis(): 
    # Try catch block to ensure user enters suitable alpha and beta values
    numberGraphs = float(input("How many graphs would you like plotted? \nEnter 1 for 1 and 2 for many\n"))

    if numberGraphs == 1:
        generateOneGraph()
    else: 
        # Can edit the set of beta distributions plotted using the "alpha_beta" variable 
        generateManyGraphs()

def generateManyGraphs():

    alpha_beta = {(10,90), (50,50)}

    for pair in alpha_beta: 
        alpha_value = pair[0]
        beta_value = pair[1]
        beta_dist = beta(alpha_value, beta_value)
        x = np.linspace(0, 1, 1000)
        beta_pdf = beta_dist.pdf(x)
        plt.plot(x, beta_pdf, label=f'PDF of Beta Distribution (α={alpha_value}, β={beta_value})')
        
    plt.ylim(0, 5)
    plt.title('PDF of Beta Distribution')
    plt.legend()
    # Get the directory of the current script
    my_path = os.path.dirname(os.path.abspath(__file__))
    # Define the path for saving the plot in the 'visuals' folder
    imagePath = os.path.join(my_path, f'visuals/graphset/betaDist_α={alpha_value}_β={beta_value}_pdf.png')

    plt.xlabel('P(H)')
    plt.ylabel('Probability Density')
    plt.savefig(imagePath)
    plt.clf()

def generateOneGraph(): 
    """Generates the pdf, cdf, and sampled histogram of a user defined beta distribution"""
    try:
        alpha_value = int(input("How many successes has the event had (int): "))
        beta_value = int(input("How many failures has the event had (int): "))
        alpha_value +=1
        beta_value +=1

        if alpha_value < 0 or beta_value < 0:
            raise ValueError("alpha and beta values must be greater than or equal to 0")
        
    except ValueError as e:
        logger.error(f"Input error: {e}")
        return  # Gracefully exit

    beta_dist = beta(alpha_value, beta_value)
    x = np.linspace(0, 1, 100)

    # Generate the PDF of the beta distribution
    beta_pdf = beta_dist.pdf(x)
    plt.plot(x, beta_pdf, label=f'PDF of Beta Distribution (α={alpha_value}, β={beta_value})')
    plt.xlabel('P(H)')
    plt.ylabel('Probability Density')
    plt.title('PDF of Beta Distribution')
    plt.legend()
    # Get the directory of the current script
    my_path = os.path.dirname(os.path.abspath(__file__))
    # Define the path for saving the plot in the 'visuals' folder
    imagePath = os.path.join(my_path, f'visuals/betaDist_α={alpha_value}_β={beta_value}_pdf.png')

    plt.savefig(imagePath)
    plt.clf()

    # plot the CDF 
    cdf_values = beta.cdf(x, alpha_value, beta_value)
    plt.plot(x, cdf_values, label=f'CDF of Beta Distribution (α={alpha_value}, β={beta_value})')
    plt.xlabel('P(X <= x)')
    plt.ylabel('Cumulative Probability Density')
    plt.legend(loc='upper left')
    imagePath = os.path.join(my_path, f'visuals/betaDist_α={alpha_value}_β={beta_value}_cdf.png')

    plt.savefig(imagePath)
    plt.clf()

    # chose discrete points with a likelihood defined by the distribution's probability density function
    n = int(input("Let's draw some samples from this distribution, chose how many samples you'd like to draw: "))

    samples = beta.rvs(alpha_value, beta_value, size=n)

    plt.hist(samples, bins=30, density=True, alpha=0.6, label='Sampled Histogram')
    plt.plot(x, beta_pdf, 'r-', lw=2, label='Beta PDF')
    plt.xlabel('x')
    plt.ylabel('Probability Density')
    plt.title(f'Sampled Histogram of {n} samples vs. Beta PDF')
    plt.legend()
    imagePath = os.path.join(my_path, f'visuals/betaDist_α={alpha_value}_β={beta_value}_pdf_histogram_overlay.png')

    plt.savefig(imagePath)