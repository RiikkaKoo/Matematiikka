import numpy as np

#1. Muunna asteiksi
# a) 2,493 rad b) 0,911 rad

a = 2.495
b = 0.911

a_asteina = np.degrees(a)
print(a_asteina)
b_asteina = np.degrees(b)
print(b_asteina)


#2. Muunna radiaaneiksi
# a) 137,7 astetta b) 62,3 astetta
print()

a = 137.7
b = 62.3

a_rad = np.radians(a)
print(a_rad)
b_rad = np.radians(b)
print(b_rad)


#3. Laadi taulukko, josta esittää seuraavat kulmat radiaaneina
# 30,45,60,90,120,135,150,180,270,360 (asteita)
print()

kulmat = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

for kulma in kulmat:
    print(f"{kulma} | {np.radians(kulma)}")