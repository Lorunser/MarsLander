import numpy as np
import matplotlib.pyplot as plt
from functools import partial
from lander.plot import plot_line_graph

def set_initials(pos_0, vel_0, t_array):
    """common to verlet and euler programs"""
    #initiliase arrays
    dims = len(pos_0)
    N = len(t_array)
    pos_array = np.empty(shape=(N, dims))
    vel_array = np.empty(shape=(N, dims))

    #set BC's
    pos_array[0] = pos_0
    vel_array[0] = vel_0

    return pos_array, vel_array, N


def euler(acc_func, pos_0, vel_0, t_array, dt):
    """Euler integrate function
    position and velocity are 3-dimensional vectors"""   
    
    pos_array, vel_array, N = set_initials(pos_0, vel_0, t_array)

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
    
    pos_array, vel_array, N = set_initials(pos_0, vel_0, t_array)

    #calcaulte second position
    pos_array[1] = pos_array[0] + vel_array[0] * dt

    #calculate vals
    for i in range(1, N-1):
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
    r = np.linalg.norm(pos)
    acceleration = - (G * M / (r ** 3)) * pos
    #print(str(pos[0]) + " | " + str(acceleration[0]))
    return acceleration  


def run():
    """run script"""
    
    # simulation time, timestep and time
    t_max = 1000
    dt = 0.5
    t_arr = np.arange(0, t_max, dt)

    # all start in same position (1000 km in x direction)
    pos_0 = np.array([1E6, 0, 0]) 

    # a) straight down descent
    a_vel_0 = np.array([0,0,0])
    a_pos_arr, a_vel_arr = verlet(acc, pos_0, a_vel_0, t_arr, dt)
    #plot_line_graph(t_arr, a_pos_arr[:,0], "Altitude (m)", title="Altitude against time", fig_number=0)

    # b) elliptic orbit
    b_vel_0 = np.array([0, 1E3, 0])
    b_pos_arr, b_vel_arr = verlet(acc, pos_0, b_vel_0, t_arr, dt)
    plot_line_graph(b_pos_arr[:,0], b_pos_arr[:,1], "y (m)", title="Elliptic orbit", fig_number=1, x_label="x (m)")
    # c) circular orbit
    # d) hyperbolic escape

    plt.show()


if __name__ == "__main__":
    run()