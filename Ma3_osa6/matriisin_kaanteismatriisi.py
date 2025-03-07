import numpy as np

matriisi1 = np.array([[3, 2, 0, -4],
                      [5, 6, 7, 1],
                      [0, -5, -1, 0],
                      [1, 3, 4, 2]])

kaanteis1 = np.linalg.inv(matriisi1)
print()
print(kaanteis1)