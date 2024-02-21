# Imports math library
import numpy as np

# Imports plotting library
import matplotlib.pyplot as plt

# Define a linear function with just one input, x
def linear_function_1D(x,beta,omega):
  # TODO -- replace the code line below with formula for 1D linear equation
  y = beta + omega * x

  return y
# Plot the 1D linear function

# Define an array of x values from 0 to 10 with increments of 0.01
# https://numpy.org/doc/stable/reference/generated/numpy.arange.html
x = np.arange(0.0,10.0, 0.01)

# Compute y using the function you filled in above
beta = 1.0; omega = 2.0

y = linear_function_1D(x,beta,omega)

# Plot this function
fig, ax = plt.subplots()

ax.plot(x,y,'r-')

ax.set_ylim([0,10]);ax.set_xlim([0,10])

ax.set_xlabel('x'); ax.set_ylabel('y')

plt.show

# TODO -- experiment with changing the values of beta and omega
# to understand what they do.  Try to make a line
# that crosses the y-axis at y=10 and the x-axis at x=5


