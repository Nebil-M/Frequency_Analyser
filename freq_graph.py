import io_functions_analyse as fi
import matplotlib.pyplot as plt
import numpy as np
import pickle
from io_functions_analyse import load

## MATPLOTLIB
fig, ax = plt.subplots()

e = load("Eng", path='')

def graph(obj, step=100):
    x = np.arange(0, obj.unique_lemmas, step)
    y = list(map(lambda i: obj.word_coverage(i)[1], x))
    plt.xscale("log")
    a = ax.plot(x, y)

fi.load('Eng_graph', path='Data/Graphs/')

plt.show()