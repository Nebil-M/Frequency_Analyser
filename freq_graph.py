import matplotlib.pyplot as plt
import numpy as np
from io_functions_analyse import*

# MATPLOTLIB

def graph(*objs, step=100, title=None, log=True):
    fig, ax = plt.subplots()

    ax.set_xscale("log") if log else None
    ax.set_xlabel('Unique Lemmas', fontsize=12)
    ax.set_ylabel('Percent Coverage', fontsize=12)
    ax.set_title(title, fontsize=20)
    ax.grid(True)

    for obj in objs:
        x = np.arange(0, obj.unique_lemmas, step)
        y = list(map(lambda i: obj.word_coverage(i)[1], x))
        ax.plot(x, y, label=str(type(obj).__name__)[-9::-1][::-1])
    ax.legend()


timing(lambda: graph(fr, es, en, step=1, title="Percent coverage vs Unique lemmas", log=True))

plt.show()
