import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from analyse import *
from io_functions_analyse import load

## MATPLOTLIB
fig, ax = plt.subplots()  # Create a figure containing a single axes.

e = load("Eng")
x = []
y = []
t = e.unique_lemmas
for i in range(0, t, 100):
    x.append(i)
    y.append(e.word_coverage(i)[1])
ax.plot(x, y)  # Plot some data on the axes.

#
es = load("ES")
x = []
y = []
t = es.unique_lemmas
for i in range(0, t, 100):
    x.append(i)
    y.append(es.word_coverage(i)[1])
ax.plot(x, y)  # Plot some data on the axes.

#
f = load("FR")
x = []
y = []
t = f.unique_lemmas
for i in range(0, t, 100):
    x.append(i)
    y.append(f.word_coverage(i)[1])

ax.plot(x, y)  # Plot some data on the axes.
plt.show()