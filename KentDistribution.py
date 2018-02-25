'''

Research Project:
Reliability Assessment of Rock Slopes by Discrete
Elements and Random Sets
Universidad Nacional de Colombia sede Bogota
Author: Rodrigo Hernandez-Carrillo
2/8/18

# Copyright (c) Rodrigo Hernandez-Carrillo 2018

___________________________________________________

This computes the parameters of a Kent distribution.
As input it requires the rotation and orientation matrices.

Procedure followed as described by Fisher, Lewis and Embleton, 1987
'''

import numpy as np

# Function to compute the parameters of Kent distribution, from a given
# set of data
# Input: orientation matrix, rotation matrix, number of planes and mean
# resultant
# Output: kappa: concentration parameter. Beta: Ovalness. Major and minor
# axis.
# Ref. Fisher, Lewis and Embleton, 1987. Section 5.3

class KentDistribution ():



    def EstimationKenParameters (self, ori_mat, rot_mat, n, mean_res):
        S = ori_mat * 1/n
        B = np.dot(np.transpose(rot_mat), np.dot(S,rot_mat))
        psi = 0.5 * np.arctan(2*B[1,2] / (B[1, 1] - B[2, 2]))
        k = (1, 0, 0, 0, np.cos(psi), -np.sin(psi), 0, np.sin(psi), np.cos(psi))
        k = np.asarray(k).reshape(3,3 )
        g = np.dot(rot_mat, k)
        v = np.dot(np.transpose(g), np.dot(S,g))
        q = v[1, 1] - v[2, 2]
        kappa = 1 / (2 - 2*mean_res - q) + 1 / (2 - 2*mean_res + q)
        beta = np.abs(0.5*(1 / (2 - 2*mean_res - q) - 1 / (2 - 2*mean_res +
                                                           q)))
        print("S", S, "B", B, "G", g, "V", v)
        return g, kappa, beta

if __name__ == "__main__":
    exit






