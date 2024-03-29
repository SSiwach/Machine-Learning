%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.random.rand(100,1)

y = 2*x+np.random.randn(100,1)

linreg = LinearRegression()

linreg.fit(x,y)

xnew = np.array([[0],[1]])

ypredict = linreg.predict(xnew)

plt.plot(xnew, ypredict, "r-")

plt.plot(x,y,'ro')

plt.axis([0,1.0,0,5.0])

plt.xlabel(r'x')

plt.ylabel(r'y')

plt.title(r'Simple Lienar Regression')

plt.show()
