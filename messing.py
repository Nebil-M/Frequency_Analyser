from io_functions_analyse import *
from analyse import*


a = load_corpus('Eng')
idx=10

for i in range(1000):
    print(a.n_common_words(idx) == a.unique_lemma_freq_list[0:idx])


