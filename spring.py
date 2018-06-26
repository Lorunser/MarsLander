import numpy as np
import matplotlib.pyplot as plt


def euler_sim(m, k, x0, v0, dt, t_array):
    """Run euler simulation to numerically integrate mass on a spring from given initial conditions"""
    # initialise empty lists to record trajectories
    x_list = []
    v_list = []

    # set initial conditions
    x = x0
    v = v0

    # Euler integration
    for t in t_array:

        # append current state to trajectories
        x_list.append(x)
        v_list.append(v)

        # calculate new position and velocity
        a = -k * x / m
        x = x + dt * v
        v = v + dt * a

    # convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
    x_array = np.array(x_list)
    v_array = np.array(v_list)

    return x_array, v_array


def verlet_sim(m, k, x0, v0, dt, t_array):
    """Run verlet simulation on mass on a spring form given boundary conditions"""
    #initiliase arrays
    x_array = np.zeros_like(t_array)
    v_array = np.zeros_like(t_array)
    n = len(t_array)

    #set initial conditions on x
    x_array[0] = x0
    x_array[1] = x0 + v0 * dt

    # initial conditions for v
    v_array[0] = v0

    for i in range(1, n - 1):       
        # verlet integration for x
        a_i = -k * x_array[i] / m
        x_array[i+1] = (2 * x_array[i]) - (x_array[i-1]) + ((dt ** 2) * a_i)

        # differentiation for v
        v_array[i] = (x_array[i+1] - x_array[i-1]) / (2 * dt)

    #set final v
    v_array[n-1] = (x_array[n-1] - x_array[n-2]) / dt

    return x_array, v_array
    

def plot(t_array, x_array, v_array, title, fig_number):
    # plot the position-time graph
    plt.figure(fig_number)
    plt.title(title)
    plt.clf()
    plt.xlabel('time (s)')
    plt.grid()
    plt.plot(t_array, x_array, label='x (m)')
    plt.plot(t_array, v_array, label='v (m/s)')
    plt.legend()


def run():
    # mass, spring constant, initial position and velocity
    m = 1
    k = 1
    x0 = 0
    v0 = 1

    # simulation time, timestep and time
    t_max = 100
    dt = 0.1
    t_array = np.arange(0, t_max, dt)

    # run Euler sim
    euler_x_array, euler_v_array = euler_sim(m, k, x0, v0, dt, t_array)
    plot(t_array, euler_x_array, euler_v_array, "Euler simulation", 1)

    # run Verlet sim
    verlet_x_array, verlet_v_array = verlet_sim(m, k, x0, v0, dt, t_array)
    plot(t_array, verlet_x_array, verlet_v_array, "Verlet simulation", 2)

    # display both figures
    plt.show()


if __name__ == "__main__":
    run()
