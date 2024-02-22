import numpy as np
import matplotlib.pyplot as plt

# size of matrix, time in us
time_np_1 = np.array([
    [128,   311],
    [256,   1170],
    [512,   7510],
    [1024,  34100],
    [2048,  206000]
])

time_cp_1 = np.array([
    [128,   74.6],
    [256,   76.7],
    [512,   252],
    [1024,  1080],
    [2048,  4170],
])

time_np_2 = np.array([
    [128,   235],
    [256,   1150],
    [512,   6550],
    [1024,  28700],
    [2048,  186000]
])

time_cp_2 = np.array([
    [128,   162],
    [256,   74.2],
    [512,   74.4],
    [1024,  230],
    [2048,  957],
])

plt.figure(figsize = (13, 8))
plt.plot(time_np_1[:, 0], time_np_1[:, 1], 'k-', label = 'Numpy float64')
plt.plot(time_cp_1[:, 0], time_cp_1[:, 1], 'k-.', label = 'Cupy float64')
plt.plot(time_np_2[:, 0], time_np_2[:, 1], 'r-', label = 'Numpy float32')
plt.plot(time_cp_2[:, 0], time_cp_2[:, 1], 'r-.', label = 'Cupy float32')

plt.legend()
plt.yscale('log')
plt.xscale('log', base=2)
plt.xlabel('n')
plt.ylabel('Time [us]')

plt.savefig('results.pdf')
plt.show()
