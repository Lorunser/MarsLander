import numpy as np
import matplotlib.pyplot as plt
from functools import partial


def euler(acc_func, pos_0, vel_0, t_array, dt):
    """Euler integrate function
    position and velocity are 3-dimensional vectors"""
    
    #initiliase arrays
    pos_array = np.empty(N)
    vel_array = np.empty(N)
    N = len(t_array)

    #set BC's
    pos_array[0] = pos_0
    vel_array[0] = vel_0

    #calculate vals
    for i in range(0, N-1):
        #calculate acceleration
        acc_i = acc_func(pos_array[i])

        # calculate new vals from previous
        vel_array[i + 1] = vel_array[i] + acc_i * dt
        pos_array[i + 1] = pos_array[i] + vel_array[i] * dt

    return pos_array, vel_array


def verlet(acc_func, pos_0, vel_0, t_array, dt):
    """verlet integrate function"""
    #initiliase arrays
    N = len(t_array)
    pos_array = np.empty(N)
    vel_array = np.empty(N)

    #set BC's
    pos_array[0] = pos_0
    vel_array[0] = vel_0

    #calculate vals
    for i in range(0, N-1):
        #calculate acceleration
        acc_i = acc_func(pos_array[i])
        # calculate new position from previous
        pos_array[i + 1] = (2 * pos_array[i]) - (pos_array[i - 1]) +  ((dt ** 2) * acc_i)
        #differentiate for velocity
        vel_array[i] = (pos_array[i+1] - pos_array[i-1]) / (2 * dt)

    #set final vel
    vel_array[N - 1] = (pos_array[N - 1] - pos_array[N - 2]) / dt

    return pos_array, vel_array


def acc(pos, G=6.67E-11, M=6.42E23):
    r = np.sqrt(pos.dot(pos))
    acceleration = G * M * pos / (r ** 3)
    return acceleration  


def run():
    """run script"""


if __name__ == "__main__":
    run()