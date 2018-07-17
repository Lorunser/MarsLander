import numpy as np
import matplotlib.pyplot as plt
import os

cwd = os.path.dirname(__file__)
filename = os.path.join(cwd, 'c++', 'simulation-project', 'simulation-project', 'trajectories.txt')
results = np.loadtxt(filename)
plt.figure(1)
plt.clf()
plt.xlabel('time (s)')
plt.grid()
plt.plot(results[:, 0], results[:, 1], label='x (m)')
plt.plot(results[:, 0], results[:, 2], label='v (m/s)')
plt.legend()
plt.show()