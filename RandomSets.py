#  Code Rodrigo

'''
This script computes the cumulative probability curves
(Dempster-Shafer strcutures) from the convolution results given
by the propagation of uncertaunty thru the model.
'''


import numpy as np
import matplotlib.pyplot as plt

def random_sets(lower, lowprob, upper, upperprob):
    lower_sorted = lower[lower.argsort()]
    lower_probability = np.cumsum(lowprob)
    upper_sorted = upper[upper.argsort()]
    upper_probability = np.cumsum(upperprob)
    return lower_sorted, lower_probability, upper_sorted, upper_probability

if __name__ == "__main__":
    exit