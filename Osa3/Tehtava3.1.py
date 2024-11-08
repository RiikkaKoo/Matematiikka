# Aiemmassa tehtävässä piti tehdä taulukko näistä radiaaneina.
# Merkkaile nyt nämä yksikköympyrälle esimerkin mukaan: 30, 45, 60, 90, 120, 150, 180, 270.

from matplotlib import pyplot as plt, patches
import numpy as np


fig = plt.figure()
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])

kulma_rad = np.array(
    [np.radians(30), np.radians(45), np.radians(60), np.radians(90), np.radians(120), np.radians(135), np.radians(150),
     np.radians(180), np.radians(270), np.radians(360)])

text = [r'30°', r'45°', r'60°', r'90°', r'120°', r'135°', r'150°', r'180°', r'270°', r'360°']

x = np.cos(kulma_rad)
y = np.sin(kulma_rad)

plt.scatter(x, y, color='red', marker='X')

for i in range(len(kulma_rad)):
    plt.annotate(text[i],
                 xy=(np.cos(kulma_rad[i]), np.sin(kulma_rad[i])), xycoords='data',
                 xytext=(+30, +5), textcoords='offset points', fontsize=12,
                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"))

plt.show()
