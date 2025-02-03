import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
array = np.arange(-10, 11, 1)
array[array>0] = array[array>0]**3
array[array<0] = array[array<0]**2
print(array)