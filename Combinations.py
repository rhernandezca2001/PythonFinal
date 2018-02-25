#  Code Rodrigo

'''
This script, basically generates all he possible combinations
to be analyzed according to the Dempster Shafer Theory.
It requires to define beforehand, the combination of variables
that lead to the higher and lower bound for a given combination
of random sets, via the sensitivity analysis
'''

import itertools as itt
import numpy as np
import matplotlib.pyplot as plt

def read_input_RS ():
    low=np.loadtxt('LowerArray.csv', delimiter=',', skiprows=1)
    lower_bound = np.ravel(low)
    upper_bound = (np.ravel(np.transpose(np.loadtxt('UpperArray.csv',
                    delimiter=',', skiprows=1))))
    return lower_bound, upper_bound, low[0,:].size

def generate_combinations (lower, upper, n):
    lower_input = itt.combinations(lower, n)
    upper_input = np.array(list(itt.product(upper, repeat=n)))
    return lower_input, upper_input,

def independent_probability ():
    probability_assignment = (np.loadtxt('ProbabilityAssignment.csv',
                                         delimiter=',', skiprows=1))
    return probability_assignment

if __name__ == "__main__":
    a,b,r=read_input_RS ()
    #c=a[0,:].size
    d,e=generate_combinations (a,b,r)
    print(b)
    print(e)
    np.savetxt('test.out', e, delimiter=',')

#b=read_input_RS ()
#c=generate_combinations (a,b)






