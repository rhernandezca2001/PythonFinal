'''
This model basically computes the FActor of Safety of a wedge
based on the formulation of Low 1997.
This is an explicit formulation
Program developed by Rodrigo Hernández Carrillo

The program reads a vector, that includes the variables ordered as:

The variables of the problem are:

Joint dip and dip direction, from these the parameters beta and delta are computed
Joints mechanical properties:
    1. phi1: friction angle joint 1
    2. phi2: friction angle joint 2
    3. c1: cohesion joint 1
    4. c2: cohesion joint 2
    5. uweight: unit weight
    5. density: specific density of the rock
Slope geometry:
    1. h: wedge height
    2. betat: slope dip
    3. alp
    3. Omega: upper slope dip
Normalized Water Pressure, Gw1 and Gw2, which depen on the pressue distribution assumption

'''

import numpy as np


# Function to compute the factor of safety


def factor_of_safety (alpha1, beta1, alpha2, beta2, alphat, betat, phi1, c1, phi2, c2, h, omega, uweight, density ):

    dipdir1 = np.radians(alpha1)
    dip1 = np.radians(beta1)
    dipdir2 = np.radians(alpha2)
    dip2 = np.radians(beta2)
    f1 = np.radians(phi1)
    f2 = np.radians(phi2)
    dipdirT = np.radians(alphat)
    dipT = np.radians(betat)
    dipupper = np.radians(omega)

    # geometrical computations on geometry

    angle1 = np.abs(dipdir1-dipdirT)
    if angle1 < np.pi:
        delta1=dip1
    else:
        delta1= 2*np.pi - dip1

    angle2 = np.abs(dipdir2 - dipdirT)
    if angle2 < np.pi:
        delta2=dip2
    else:
        delta2= 2*np.pi - dip2

    # Computation of paramters of the model

    sin_si = np.abs(np.sqrt(1-np.power(np.sin(delta1)*np.sin(delta2)*np.cos(angle1+angle2)+np.cos(delta1)*np.cos(delta2),2)))
    tan_ep = np.sin(angle1+angle2)/(np.sin(angle1)*(1/np.tan(delta2))+np.sin(angle2)*(1/np.tan(delta1)))
    a0=sin_si/(np.power(np.sin(angle1+angle2)*np.sin(delta1)*np.sin(delta2),2)*((1/tan_ep)-(1/np.tan(dipT))))
    b1=a0*np.sin(angle2)*np.sin(delta2)
    b2=a0*np.sin(angle1)*np.sin(delta1)
    a1=(np.sin(delta2)*(1/np.tan(delta1))-np.cos(delta2)*np.cos(angle1+angle2))/(sin_si*np.sin(angle1+angle2))
    a2=(np.sin(delta1)*(1/np.tan(delta2))-np.cos(delta1)*np.cos(angle1+angle2))/(sin_si*np.sin(angle1+angle2))
    kappa=(1-np.tan(dipupper)/np.tan(dipT))/(1-np.tan(dipupper)/tan_ep)
    Gw=0.5*kappa # Pyramidal water pressure distribution
    FS = (a1 - b1*Gw/density)*np.tan(f1) + (a2 - b2*Gw/density)*np.tan(f2) + 3*b1*c1/(uweight*h) + 3*b2*c2/(uweight*h)

    return FS

if __name__=="__main__":
    print (factor_of_safety (105, 45, 235, 70, 185, 65, 30, 24, 20, 48, 30.55, 12, 25, 2.5 ))













