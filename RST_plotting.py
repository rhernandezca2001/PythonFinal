#  Code Rodrigo

'''
This code plots the cumulative probabilty functions resulting from
the
'''

import matplotlib.pyplot as plt
import numpy as np

def plot_cumulative (lower, lowprob, upper, upperprob):
    lower_output=np.repeat(lower,2)
    lower_probability=np.repeat(lowprob,2)
    plt.plot(lower_output[1:], lower_probability[:-1],'g-', linewidth=2.0 )
    #plt.figure()
    upper_output = np.repeat(upper, 2)
    upper_probability = np.repeat(upperprob, 2)
    plt.plot(upper_output[1:], upper_probability[:-1], 'g-', linewidth=2.0)
    plt.ylim(0, 1)
    plt.xlabel('Factor of Safety')
    plt.ylabel('Cumulative Probability')
    plt.show()
    return

if __name__ == "__main__":
    exit