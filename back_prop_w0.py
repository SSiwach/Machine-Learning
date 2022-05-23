x = [1.0,-2.0,3.0]
w = [-3.0,-1.0,2.0]
b = 1.0
y = [0,0,0]
z = 0
for i in range(len(x)):
  y[i] = x[i]*w[i]
  print(y[i])
  z += y[i]
  zmax = max(z,0)

dvalue  = 1.0
drelu_dz = dvalue*(1. if z > 0 else 0.)

print(drelu_dz)
print(z+b)

dsum_dxw0 = 1
dsum_dxw1 = 1
dsum_dxw2 = 1

dsum_db = 1


drelu_dxw0 = drelu_dz*dsum_dxw0
drelu_dxw1 = drelu_dz*dsum_dxw1
drelu_dxw2 = drelu_dz*dsum_dxw2

drelu_db = drelu_dz*dsum_db

print(drelu_dxw0, drelu_dxw1, drelu_dxw2, drelu_db)


print(drelu_dxw0)

dmul_dx0 = w[0]
drelu_dx0 = drelu_dxw0*dmul_dx0
print(drelu_dx0)
