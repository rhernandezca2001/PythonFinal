'''

Research Project:
Reliability Assessment of Rock Slopes by Discrete
Elements and Random Sets
Universidad Nacional de Colombia sede Bogota
Author: Rodrigo Hernandez-Carrillo
2/8/18

# Copyright (c) Rodrigo Hernandez-Carrillo 2018

___________________________________________________


This class computes the main geometruical features of an input set of
directional data expressed in terms of a 2 columns array. The fisrt
column corresponds to the dip direction, while the second one to the dip
of a plane.

Functions to compute the mean, resultant, orientation matrix and
rotation matrix are provided.

'''

import numpy as np


# Function to read input matrix
# Output: array of planes expressed as dip direction and dip in degrees


def open_array(filename, suffix):
    input_file = '{}{}{}'.format(filename, '.', suffix)
    input_array = np.loadtxt(input_file, delimiter=',', skiprows=1)
    return input_array


# When required, the following function modifies the angles to
# longitude and colaitude. Recommended for computing Kent distribution
# paraneters.
# Input: array in dip and dip direction
# Output: inout angles in terms of colatitude and longitude


def angle_adjustment(input_angle):
    input_angle[:, 1] = 90 - input_angle[:, 1]
    print(input_angle)
    return input_angle


# Function to compute the direction cosines.
# this transformation can be utilized when the axis are defined as follows:
# 1. Angles given in colatitude and longitude.
# 2. Colatitude measure with respct to axis x1.
# 3. The  longitude is measured clockwise from x2.
# See Kasarapu 2015
# Input: input array of planes expressed as dip direction and dip in
# degrees
# Output: number of planes, vector wih coordinates direction
# cosines, orientation matrix.
# Ref. Fisher, Lewis and Embleton, 1987

def direction_cosines(in_array):
    n = np.ma.size(in_array, axis=0)  # number of measured planes
    cos_x1 = np.cos(np.radians(in_array[:, 1]))
    cos_x2 = (np.cos(np.radians(in_array[:, 0])) *
              np.sin(np.radians(in_array[:, 1])))
    cos_x3 = (np.sin(np.radians(in_array[:, 0])) *
              np.sin(np.radians(in_array[:, 1])))
    orientation_matrix = (np.sum(cos_x1 ** 2), np.sum(cos_x1 * cos_x2),
                          np.sum(cos_x1 * cos_x3), np.sum(cos_x1 * cos_x2),
                          np.sum(cos_x2 ** 2),
                          np.sum(cos_x2 * cos_x3), np.sum(cos_x1 * cos_x3),
                          np.sum(cos_x2 * cos_x3),
                          np.sum(cos_x3 ** 2))
    orientation_matrix = np.asarray(orientation_matrix).reshape(3, 3)
    print("This is the orientation matrix", orientation_matrix)
    return n, cos_x1, cos_x2, cos_x3, orientation_matrix


# Function to compute the mean direction in dip and dip directions
# Input: direction cosines
# Output: Resultant length R, mean resultant length, mean unit vector,
# mean dip direction and dip in degrees

def sample_mean(cos_x1, cos_x2, cos_x3):
    n = np.ma.size(cos_x1, axis=0)
    sum_x1 = np.sum(cos_x1)
    sum_x2 = np.sum(cos_x2)
    sum_x3 = np.sum(cos_x3)
    resultant = np.sqrt(sum_x1 ** 2 + sum_x2 ** 2 + sum_x3 ** 2)
    mean_resultant = resultant / n
    mean_unit_vector = (
    sum_x1 / resultant, sum_x2 / resultant, sum_x3 / resultant)

    if mean_unit_vector[1] >= 0 and mean_unit_vector[2] >= 0:
        Q = (-2 * np.degrees(np.arctan(np.abs(mean_unit_vector[
                                                 2] /
                                             mean_unit_vector[
                                                 1]))) + 180)
    else:
        if mean_unit_vector[1] >= 0 and mean_unit_vector[2] < 0:
            Q = (-2 * np.degrees(np.arctan(np.abs(mean_unit_vector[
                                                 2] /
                                             mean_unit_vector[
                                                 1]))) + 360)
        else:
            Q = 180

    mean_angle1 = (np.degrees(np.arctan(np.abs(mean_unit_vector[
                                                   2] / mean_unit_vector[
                                                   1]))) + Q)
    mean_angle2 = np.degrees(np.arccos(mean_unit_vector[0]))
    return resultant, mean_resultant, mean_unit_vector, mean_angle1, \
           mean_angle2


# Function to compute the rotation matrix (transformation matrix)
# Input: Dip and dip direction of the new axis in degrees
# Output: rotation matrix
# Ref. Fisher, Lewis and Embleton, 1987

def rotation_matrix(ang1, ang2):
    rotation_matrix = (np.cos(np.radians(ang2)), -np.sin(np.radians(
        ang2)), 0, np.sin(np.radians(ang2)) * np.cos(np.radians(ang1)),
                       np.cos(np.radians(ang1)) * np.cos(np.radians(ang2)),
                       -np.sin(np.radians(ang1)),
                       np.sin(np.radians(ang2)) * np.sin(np.radians(ang1)),
                       np.sin(np.radians(ang1)) * np.cos(np.radians(ang2)),
                       np.cos(np.radians(ang1)))
    rotation_matrix = np.asarray(rotation_matrix).reshape(3, 3)
    print("This is the rotation matrix", rotation_matrix)
    return rotation_matrix


if __name__ == "__main__":
    exit
