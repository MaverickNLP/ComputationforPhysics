import numpy as np

def f(x): 

  return np.e**(-x**2) # Forgot to get e from np.

count = 0 # I honestly forgot all the random functions so I’m going off what I know from the quiz. 

y_array = [] 

N = 1000000

while count <= int(N): 

  x = np.random.rand()

  y_array.append(f(x))

  count += 1

b = 1

a = 0

integral_est = (b-a)*np.mean(y_array)

print(integral_est)