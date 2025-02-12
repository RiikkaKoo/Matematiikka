import numpy as np
import numpy.linalg as la #Laskee matriisin käänteismatriisin

from sympy import solve, symbols

#T 8.1.1
#v) {2x-3y=5, 7x+y=3}
"""
#Ratkaisu käyttämällä Numpy-kirjastoa:
a = np.array([[2,-3],[7,1]])
b = np.array([[5],[3]])

x = la.inv(a).dot(b)

print(x)
"""

#Ratkaisu käyttämällä Sympy-kirjastoa:
x, y = symbols('x, y')
v1 = solve([2*x - 3*y - 5,
       7*x + y - 3], [x,y])

print("8.1.1 v):", v1)

#a) {2x+3y=11, 7x-y=4}
x, y = symbols('x, y')
v2 = solve([2*x + 3*y - 11,
       7*x - y - 4], [x,y])

print("8.1.1 a):", v2)

print()
#T 8.1.2
#v) {3x-y+5z=2, 7x+2y+3z=9, 4x+y-7z=5}
x, y, z = symbols('x, y, z')
v3 = solve([3*x - y + 5*z - 2,
            7*x + 2*y + 3*z - 9,
            4*x + y - 7*z - 5], [x,y,z])

print("8.1.2 v):", v3)

#a) {2x+y-3z=5, -3x-y+2z=-7, 5x+2y-4z=12}
x, y, z = symbols('x, y, z')
v4 = solve([2*x + y - 3*z - 5,
            -3*x - y + 2*z - -7,
            5*x + 2*y - 4*z - 12], [x,y,z])

print("8.1.2 a):", v4)

print()
#T 8.1.3
#v1) {x+y+z=3, 2x+y-z=2, 4x+3y+z=5}
x, y, z = symbols('x, y, z')
v5 = solve([x + y + z - 3,
            2*x + y - z - 2,
            4*x + 3*y + z - 5], [x,y,z])

print("8.1.3 v1):", v5, "Ei ratkaisua")

#v2) {x+y+z=3, 2x+y-z=2, 4x+3y+z=8}
x, y, z = symbols('x, y, z')
v6 = solve([x + y + z - 3,
            2*x + y - z - 2,
            4*x + 3*y + z - 8], [x,y,z])

print("8.1.3 v2):", v6, ", z on mielivaltainen")

#a) {2x+y-3z=5, -3x-y+2z=-7, 5x+2y-5z=12}
x, y, z = symbols('x, y, z')
v7 = solve([2*x + y - 3*z - 5,
            -3*x - y + 2*z - -7,
            5*x + 2*y - 5*z - 12], [x,y,z])

print("8.1.3 a):", v7, ", z on mielivaltainen")

#b) {2x+y-3z=5, -3x-y+2z=-7, 5x+2y-5z=11}
x, y, z = symbols('x, y, z')
v8 = solve([2*x + y - 3*z - 5,
            -3*x - y + 2*z - -7,
            5*x + 2*y - 5*z - 11], [x,y,z])

print("8.1.3 b):", v8, "Ei ratkaisua")