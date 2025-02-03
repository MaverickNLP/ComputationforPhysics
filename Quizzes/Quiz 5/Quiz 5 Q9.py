import random as rnd 
import numpy as np # My environment always as numpy loaded I don't usually have to call this manually I forgot :((

N = 1000

sample_space = np.linspace(0, N, N+1, True) # I’m making a list of [0, 1, 2, …, 1000]

output = []

red = 0

blue = 0 

green = 0

for i in sample_space:

  out = rnd.choice([0, 0, 0, 1, 1, 1, 1, 1, 2, 2]) # I imported random as rnd 

  if out == 0:

    red += 1

  elif out == 1:

    blue +=1

  elif out ==2:

    green += 1

prob_red = red/N

prob_blue = blue/N

prob_green = green/N

print("The probability of drawing red from this bag is     ", prob_red) # the commas won't work due to wierd interfacing, and I forgot a comma between different print terms.

print("The probability of drawing blue from this bag is     ", prob_blue)

print("The probability of drawing green from this bag is     ",prob_green)