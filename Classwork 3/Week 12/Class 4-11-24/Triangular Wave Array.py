import numpy as np
import matplotlib.pyplot as plt

def triangle_wave(start, end, step):
	x_array= np.arrange(start, end, end/step+1)
	return x_array



print(triangle_wave(0, 50, 2))