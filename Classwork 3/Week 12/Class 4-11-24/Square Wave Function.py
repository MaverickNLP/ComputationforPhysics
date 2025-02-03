import numpy as np
import matplotlib.pyplot as plt

def square_wave(start, end, step=1):
    # Generate values between start and end with the specified step
    values = np.arange(start, end, step)
    # Create the square wave pattern by alternating 0s and 1s
    square_wave_array = (values % 2).astype(int)
    return square_wave_array

# Example usage for range [0, 10]
square_wave_array = square_wave(0, 12)
print(square_wave_array)