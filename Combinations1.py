#  Code Rodrigo

'''
This script, basically generates all he possible combinations
to be analyzed according to the Dempster Shafer Theory.
It requires to define beforehand, the combination of variables
that lead to the higher and lower bound for a given combination
of random sets, via the sensitivity analysis
'''


import numpy as np
from WedgeFoS import factor_of_safety
from RandomSets import random_sets
from RST_plotting import plot_cumulative

def read_input_RS ():
    lower_bound = np.transpose(np.loadtxt('LowerArray.csv', delimiter=',', skiprows=1))
    upper_bound = np.transpose(np.loadtxt('UpperArray.csv', delimiter=',', skiprows=1))
    return lower_bound, upper_bound


def cartesian(arrays):
    arrays = [np.asarray(a) for a in arrays]
    shape = (len(x) for x in arrays)

    ix = np.indices(shape, dtype=float)
    ix = ix.reshape(len(arrays), -1).T

    for n, arr in enumerate(arrays):
        ix[:, n] = arrays[n][ix.astype(int)[:, n]]

    return ix


def read_probability_assignment ():
    lower_assignment = np.transpose(np.loadtxt('LowerProbabilityAssignment.csv', delimiter=',', skiprows=1))
    upper_assignment = np.transpose(np.loadtxt('UpperProbabilityAssignment.csv', delimiter=',', skiprows=1))
    return lower_assignment, upper_assignment

def independent_probabilty (probability_assigment):

    output_probability = np.product(probability_assigment, axis=1)
    return output_probability

if __name__ == "__main__":
    a,b=read_input_RS ()
    low_probability, up_probability=read_probability_assignment ()
    c=cartesian(b)
    d=cartesian(b)
    lower_assignment_combination=cartesian(low_probability)
    print(lower_assignment_combination)
    independent_lower=independent_probabilty (lower_assignment_combination)
    upper_assignment_combination = cartesian(up_probability)
    independent_upper = independent_probabilty(upper_assignment_combination)
    print(c.shape)
    print(d)
    FOS1 = factor_of_safety(105, 45, 235, 70, 185, 65, 30, 24, 20, 48, 30.55, c[:,2], 25, c[:,1])
    FOS1A = factor_of_safety(105, 45, 235, 70, 185, 65, 10, 24, 20, 48, 30.55, c[:, 2], 25, c[:, 1])
    FOS2 = factor_of_safety(105, 45, 235, 70, 185, 65, 12, 24, 20, 48, 30.55, c[:, 2], 25, c[:, 1])
    FOS2A = factor_of_safety(105, 45, 235, 70, 185, 65, 43, 24, 20, 48, 30.55, c[:, 2], 25, c[:, 1])

    print (FOS1, FOS1A, FOS2, FOS2A)
    FOS1,low,FOS2, upper= random_sets(FOS1,independent_lower, FOS2, independent_upper )
    print(FOS1,low,  FOS2, upper)
    df=plot_cumulative(FOS1,low,  FOS2, upper)




