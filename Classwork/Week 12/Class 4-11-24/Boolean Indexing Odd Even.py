import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
rand_arr = random.randint(0, 101, 50)
rand_arr_2mod = rand_arr%2
rand_arr_2modTF = rand_arr_2mod==True
rand_arr_2mod1 = -(rand_arr%2 - 1)
rand_arr_2mod1TF = rand_arr_2mod1==True
print(rand_arr[rand_arr_2mod1TF])
print (rand_arr[rand_arr_2modTF])
