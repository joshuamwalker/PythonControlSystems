import numpy as np
from random import seed
from random import random

whiteNoise = np.random.rand(20) - 0.5
n = whiteNoise.shape
print(whiteNoise[3])

randomWalk = np.zeros(n)
print(randomWalk[3] if 5 == 5 else 4)


import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)


N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()
