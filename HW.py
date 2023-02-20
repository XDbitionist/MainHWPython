import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f(x):
    return -12*x**4*np.sin(np.cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30

# Task 1: Find roots
roots = fsolve(f, [-5, -3, 0, 2, 4])
print("Roots:", roots)

# Task 2: Find intervals where f(x) is increasing
increasing_intervals = []
for i in range(len(roots) - 1):
    x = np.linspace(roots[i], roots[i+1], 1000)
    y = f(x)
    if all(y[i] < y[i+1] for i in range(len(y)-1)):
        increasing_intervals.append((roots[i], roots[i+1]))
print("Increasing intervals:", increasing_intervals)

# Task 3: Find intervals where f(x) is decreasing
decreasing_intervals = []
for i in range(len(roots) - 1):
    x = np.linspace(roots[i], roots[i+1], 1000)
    y = f(x)
    if all(y[i] > y[i+1] for i in range(len(y)-1)):
        decreasing_intervals.append((roots[i], roots[i+1]))
print("Decreasing intervals:", decreasing_intervals)

# Task 4: Plot the function
x = np.linspace(-5, 5, 1000)
y = f(x)
plt.plot(x, y)
plt.axhline(y=0, color='k', lw=0.5)
plt.axvline(x=0, color='k', lw=0.5)
plt.title("f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

# Task 5: Find the vertex
a, b, c, d, e = -12, -18, 5, 10, -30
x_vertex = -b / (3 * a)
y_vertex = f(x_vertex)
print("Vertex:", (x_vertex, y_vertex))

# Task 6: Find intervals where f(x) > 0
positive_intervals = []
for i in range(len(roots) - 1):
    x = np.linspace(roots[i], roots[i+1], 1000)
    y = f(x)
    if all(y[i] > 0 for i in range(len(y))):
        positive_intervals.append((roots[i], roots[i+1]))
print("Intervals where f(x) > 0:", positive_intervals)

# Task 7: Find intervals where f(x) < 0
negative_intervals = []
for i in range(len(roots) - 1):
    x = np.linspace(roots[i], roots[i+1], 1000)
    y = f(x)
    if all(y[i] < 0 for i in range(len(y))):
        negative_intervals.append((roots[i], roots[i+1]))
print("Intervals where f(x) < 0:", negative_intervals)
