# Kuvan oletuskoko 6.4 * 4.8 tuumaa. Haluat tehdä kuvaajan väliltä -3π - 3π.
# Levennä kuva kolminkertaiseksi ja vaihdä käyrien värit sekä piirtotyyli.
# Lisää myöskin kuvaan selite.

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-3*np.pi, 3*np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X,C)
plt.plot(X,S)

plt.figure(figsize=(3*6.4,4.8), dpi=80)
plt.plot(X, C, color="teal", linewidth=3, linestyle=":")
plt.plot(X, S, color="purple",  linewidth=3, linestyle=":")

plt.plot(X, C, color="teal", linewidth=3, linestyle=":", label="cos")
plt.plot(X, S, color="purple",  linewidth=3, linestyle=":", label="sin")

plt.legend(loc='upper left', frameon=False)

plt.show()