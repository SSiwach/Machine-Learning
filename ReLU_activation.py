


x = [1.0,-2.0,3.0]
w = [-3.0,-1.0,2.0]
b = 1.0
y = [0,0,0]
z = 0
for i in range(len(x)):
  y[i] = x[i]*w[i]
  print(y[i])
  z += y[i]

print(z+b)
