# This problem was asked by Google.

# The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
# Hint: The basic equation of a circle is x ** 2 + y ** 2 = r ** 2.

from random import random
import matplotlib.pyplot as plt

inside = 0
n = 10000
x_inside, y_inside, x_outside, y_outside  = ([] for i in range(4))

for i in range(n):
    x, y = random(), random()
    if x ** 2 + y ** 2 <= 1:
        inside += 1
        x_inside.append(x)
        y_inside.append(y)
    else:
        x_outside.append(x)
        y_outside.append(y)

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.scatter(x_inside, y_inside, color='b', marker='s')
ax.scatter(x_outside, y_outside, color='r', marker='s')
fig.show()

pi = (4 * inside) / n
print(round(pi, 3))
