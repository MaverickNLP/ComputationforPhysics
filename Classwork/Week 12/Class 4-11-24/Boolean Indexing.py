import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
random_arr = random.randint(0, 101, 50)
rand_arr_croc50 = random_arr>50
print(random_arr, rand_arr_croc50)
random_arr[rand_arr_croc50] = 50
print(random_arr)