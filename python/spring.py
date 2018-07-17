import numpy as np
import math
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
    N = len(t_array)
    x_array = np.empty(N)
    v_array = np.empty(N)

    #set initial conditions on x
    x_array[0] = x0
    x_array[1] = x0 + v0 * dt

    # initial conditions for v
    v_array[0] = v0

    for i in range(1, N - 1):       
        # verlet integration for x
        a_i = -k * x_array[i] / m
        x_array[i+1] = (2 * x_array[i]) - (x_array[i-1]) + ((dt ** 2) * a_i)

        # differentiation for v
        v_array[i] = (x_array[i+1] - x_array[i-1]) / (2 * dt)

    #set final v
    v_array[N-1] = (x_array[N-1] - x_array[N-2]) / dt

    return x_array, v_array


def analytic_soln(m, k, x0, v0, t_array):
    """computes analytical solution"""
    # general solution of form: 
    # x = a cos wt + b sin wt
    # v = -wa sin wt + wb cos wt

    # set constants
    w = math.sqrt(k / m)
    a = x0
    b = v0 / w

    x_func = lambda t : a * math.cos(w * t) + b * math.sin(w * t)
    v_func = lambda t : w * (- a * math.sin(w * t) + b * math.cos(w * t))

    #casting to list necessary as map returns an iterable
    x_array = np.array(list(map(x_func, t_array)))
    v_array = np.array(list(map(v_func, t_array)))

    #alternative method
    #x_array = np.array([x_func(ti) for ti in t_array])
    #v_array = np.array([v_func(ti) for ti in t_array])

    return x_array, v_array


def plot(t_array, x_array, v_array, title, fig_number, label_1 = 'x (m)', label_2 = 'v (m/s)'):
    # plot the position-time graph
    plt.figure(fig_number)
    plt.title(title)
    plt.xlabel('time (s)')
    plt.grid()
    plt.plot(t_array, x_array, label=label_1)
    plt.plot(t_array, v_array, label=label_2)
    plt.legend()


def run():
    # mass, spring constant, initial position and velocity
    m = 1
    k = 1
    x0 = 0
    v0 = 1

    # simulation time, timestep and time
    t_max = 100
    dt = 0.2
    t_array = np.arange(0, t_max, dt)

    # run Euler sim
    #euler_x_array, euler_v_array = euler_sim(m, k, x0, v0, dt, t_array)
    #plot(t_array, euler_x_array, euler_v_array, "Euler simulation", 1)

    # run Verlet sim
    verlet_x_array, verlet_v_array = verlet_sim(m, k, x0, v0, dt, t_array)
    plot(t_array, verlet_x_array, verlet_v_array, "Verlet simulation", 2)

    # run analytic simulation
    #analytic_x_array, analytic_v_array = analytic_soln(m, k, x0, v0, t_array)
    #plot(t_array, analytic_x_array, analytic_v_array, "Analytic solution", 3)

    # display errors
    #euler_error = np.subtract(euler_x_array, analytic_x_array)
    #verlet_error = np.subtract(verlet_x_array, analytic_x_array)
    #plot(t_array, euler_error, verlet_error, "Error in solution", 4, "Euler", "Verlet")


    # display all figures
    plt.show()


if __name__ == "__main__":
    run()
