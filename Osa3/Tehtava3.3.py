# Akselitkin ovat vähän tylsät. Aseta akselien tekstit muoton π, π/2 jne ...

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-3 * np.pi, 3 * np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)

plt.plot(X, C)
plt.plot(X, S)

plt.figure(figsize=(3 * 6.4, 4.8), dpi=80)
plt.plot(X, C, color="teal", linewidth=3, linestyle=":")
plt.plot(X, S, color="purple", linewidth=3, linestyle=":")

plt.xlim(X.min() * 1.1, X.max() * 1.1)
plt.ylim(C.min() * 1.1, C.max() * 1.1)

plt.xticks([-3 * np.pi, -2.5 * np.pi, -2 * np.pi, -1.5 * np.pi, -np.pi, -np.pi / 2, 0, np.pi / 2, np.pi, 1.5 * np.pi,
            2 * np.pi, 2.5 * np.pi, 3 * np.pi],
           ['-3π', '-2.5π', '-2π', '-1.5π', '-π', '-π/2', '0', 'π/2', 'π', '1.5π', '2π', '2.5π', '3π'])

plt.yticks([-1, 0, +1], ['-1', '0', '+1'])

plt.plot(X, C, color="teal", linewidth=3, linestyle=":", label="cos")
plt.plot(X, S, color="purple", linewidth=3, linestyle=":", label="sin")

plt.legend(loc='upper left', frameon=False)

plt.show()
