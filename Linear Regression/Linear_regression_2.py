import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_squared_log_error, mean_absolute_error

x = np.random.rand(100,1)

y = 2.0 + 5*x + 0.5*np.random.randn(100,1) #random number generator

linreg = LinearRegression()

linreg.fit(x,y)

ypredict = linreg.predict(x)

print('The intercept alpha : \n', linreg.intercept_)

print('Coefficent beta : \n', linreg.coef_)

print("Mean squared error : %.2f" % mean_squared_error(y, ypredict))

print("Variance of score : %.2f " % r2_score(y, ypredict))

print("Mean squared log error : %.2f" % mean_squared_error(y, ypredict))

print("Mean absolute error : %.2f" % mean_absolute_error(y, ypredict))


plt.plot(x, y,'r+')

plt.plot(x, ypredict, 'ro')

plt.axis([0.0,1.0,1.5,7.0])

plt.xlabel(r'x')

plt.ylabel(r'y')

plt.title(r'Linear Regression fit ')

plt.show()
