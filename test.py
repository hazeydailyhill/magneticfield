import matplotlib.pyplot as plt
import numpy as np
from itertools import product, combinations

fig = plt.figure()



# draw vector
soa = np.array([[0, 0, 0, 1, 1, 1]])

X, Y, Z, U, V, W = zip(*soa)
ax = fig.gca(projection='3d')




ax.quiver(X, Y, Z, U, V, W)
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_title("Vectors")


plt.show()