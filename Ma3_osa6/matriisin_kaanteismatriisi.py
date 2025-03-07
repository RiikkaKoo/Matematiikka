import numpy as np
from sympy import solve, symbols

matriisi1 = np.array([[3, 2, 0, -4],
                      [5, 6, 7, 1],
                      [0, -5, -1, 0],
                      [1, 3, 4, 2]])

kaanteis1 = np.linalg.inv(matriisi1)
print()
print(kaanteis1)

matriisi2 = np.array([[7, -3, -1],
                      [-4, 9, 2],
                      [1, -2, 0]])

kaanteis2 = np.linalg.inv(matriisi2)
print()
print(kaanteis2)

print()
x, y, z = symbols('x, y, z')
vastaus = solve([7*x - 3*y -1*z - 6,
       -4*x + 9*y + 2*z - 5,
           1*x - 2*y - -8 ], [x,y,z])

print(vastaus)
print(float(vastaus[x]), float(vastaus[y]), float(vastaus[z]))