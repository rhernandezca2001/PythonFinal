#  Code Rodrigo

'''
This script generates a list of inputs and then
call the fucntions to compute the model, perform the
RST analysis and plot the cumulative probability curves
'''

import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from WedgeFoS import factor_of_safety
from RandomSets import random_sets
from RST_plotting import plot_cumulative
from Combinations1 import read_input_RS, cartesian, read_probability_assignment, independent_probabilty

# This function reads the number of

def number_of_RS ():
    n=input('Number of random sets to compare')
    n=int(n)
    return n

# This function collects several input fiels to generate a list of inputs

def input_file_list (file_name, number_RST):
    filelist=[]
    for i in range (1,2*number_RST):
        filelist.append({0},{1},{2}.format(file_name,number_RST,'.txt'))
    return filelist

# Code to loop thru a given list os files

def looping_list (function, filelist):
    for fname in filelist:
        {}({}).format(function, filelist)
    return

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

    h={}

    for i in range(0, 3):
        h['FOS{}'.format(i)]=factor_of_safety(105, 45, 235, 70, 185, 65, 30, 24, 20, 48, 30.55, c[:,i], 25, c[:,1])
        print (h)
        A, low, B, upper = random_sets(h['FOS{}'.format(i)], independent_lower, h['FOS{}'.format(i)], independent_upper)
        a=plot_cumulative(A, low, B, upper)


'''

    for i in range(1,4):

        A,low,B,upper=random_sets('FOS{}'.format(i),independent_lower, FOS2, independent_upper )



    for i in range(1,4):
        A='FOS {}'.format(i)
        B='FOS {}'.format(i+1)
        plot_cumulative(A, low, B , upper)

'''
'''
    #print (FOS1, FOS1A, FOS2, FOS2A)
    FOS1,low,FOS2, upper= random_sets(FOS1,independent_lower, FOS2, independent_upper )
    print(FOS1,low,  FOS2, upper)
    df=plot_cumulative(FOS1,low,  FOS2, upper)

'''


'''

filelist=[]

for i in range(1,5):
    filelist.append("frequency%s.dat" %i)

for fname in filelist:
    data=np.loadtxt(fname)
    X=data[:,0]
    Y=data[:,1]
    plt.plot(X,Y,':ro')

plt.show()
'''