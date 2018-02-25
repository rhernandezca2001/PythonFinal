'''

Research Project:
Reliability Assessment of Rock Slopes by Discrete
Elements and Random Sets
Universidad Nacional de Colombia sede Bogota
Author: Rodrigo Hernandez-Carrillo
2/12/18

# Copyright (c) Rodrigo Hernandez-Carrillo 2018

___________________________________________________


This script computes the input random sets corresponding to the
structural information collected. Considers:

1. Parameters computation according to Kent distribution

'''



import apsg as knt
import numpy as np
import KentDistribution as kd
import VectorMean as vm
import matplotlib


if __name__ == "__main__":

    dipdir_dip = vm.open_array('InputSet4', 'csv')
    dipdir_dip = vm.angle_adjustment(dipdir_dip )
    n, x_cos, y_cos, z_cos, orientation = vm.direction_cosines(dipdir_dip)
    r_length, r_mean, mean_vector, dipdir_mean, dip_mean = (vm.sample_mean(
        x_cos, y_cos, z_cos))
    print (mean_vector)
    rotation = vm.rotation_matrix(dipdir_mean, dip_mean)
    kent_matrix, k, beta = (kd.KenParameters(orientation, rotation, n,
                                            r_mean))
    print (kent_matrix, "kappa =", k, "beta=", beta, "mean",
           dipdir_mean,"/", dip_mean )





    kent_params = knt.Pair(141.65, 71.38, 128, 60)
    g = knt.Group.kent_lin(kent_params, 119, 43, 1000)
    r = np.array(g)
    dip_kent = np.degrees(np.arccos(r[:,2]))
    dipdir_kent = np.degrees(np.arccos(-r[:,1]/(np.sin(np.radians(
        dip_kent)))))
    c = np.stack((dipdir_kent, dip_kent), axis=1)
    # print ("Vector de puntos que se simulan", dip_kent, dipdir_kent)

    np.savetxt("KentSimulation.csv", c, delimiter=",",
               header="Dip direction, Dip", comments='')
    


    s = knt.StereoNet()
    s.contourf(g , 8, legend=True, sigma=2)
    s.line(g, 'g.')
    s.show()

    print("Este es p:", kent_params)
    print("The misfit is:", kent_params.misfit)
    print ("fvec =", kent_params.fvec)
    print("lvec =", kent_params.lvec)
    print(kent_params.fvec.cross(kent_params.lvec))
    e = kent_params.fvec.cross(kent_params.lvec)
    print(s)
    exit




