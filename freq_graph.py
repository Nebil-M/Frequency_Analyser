import io_functions_analyse as fi
import matplotlib.pyplot as plt
import numpy as np
import pickle
from io_functions_analyse import load, timing, load_corpus
import cProfile

# MATPLOTLIB
fig, ax = plt.subplots()

e = load_corpus('Eng')


def graph(obj, step=100):
    x = np.arange(0, obj.unique_lemmas, step)
    y = list(map(lambda i: obj.word_coverage(i)[1], x))
    plt.xscale("log")
    a = ax.plot(x, y)


def profile_graph(obj, step=10):
    cProfile.runctx("graph(obj, step)", globals(), locals())


timing(lambda: graph(e, 1))

plt.show()
# profile_graph(e)
