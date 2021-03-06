import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model

oecd_bli = pd.read_csv("oecd_bli_2015.csv",thousands',')
gdp_per_capita = pd.read_csv("gdp_per_capita.csv",thousands =',',delimiter='\t', encoding ='latin1',na_values"n/a)


#prepare for the data

country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)
x = np.c_[country_stats["GDP per capita"]]
y = np.c_[country_stats["Life satisfaction"]]

country_stats.plot(kind='scatter',x = "GDP per capita", y = 'life satisfication' )
plt.show()

model = sklearn.linear_model.LinearRegression()

model.fit(x,y)

X_new = [[22587]]

print(model.predict(X_new))
