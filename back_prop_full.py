x = [1.0,-2.0,3.0]
w = [-3.0,-1.0,3.0]
b = 1.0
z =0
xw = [0,0,0]
for i in range(len(x)):
  xw[i] = x[i] *w[i]
  z += xw[i]

print(z+b)

y = max(z,0)

dvalue = 1.0

drelu_dz = dvalue * (1. if z > 0 else 0)

print(drelu_dz)

dsum_dxw0 = 1
dsum_dxw1 = 1
dsum_dxw2 = 1

dsum_db = 1

drelu_dxw0 = drelu_dz * dsum_dxw0
drelu_dxw0 = drelu_dz * dsum_dxw1
drelu_dxw0 = drelu_dz * dsum_dxw2

drelu_db = drelu_dz * dsum_db
print(drelu_dxw0, drelu_dxw1, drelu_dxw2, drelu_db)

dmul_dx0 = w[0]
dmul_dx0 = w[1]
dmul_dx0 = w[2]
dmul_dw0 = x[0]
dmul_dw0 = x[1]
dmul_dw0 = x[2]
drelu_dx0 = drelu_dxw0 * dmul_dx0
drelu_dw0 = drelu_dxw0 * dmul_dw0
drelu_dx0 = drelu_dxw1 * dmul_dx1
drelu_dw0 = drelu_dxw0 * dmul_dw0
drelu_dx0 = drelu_dxw2 * dmul_dx
drelu_dw0 = drelu_dxw0 * dmul_dw0
