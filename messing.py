from analyse import *
import timeit
from main import corpus_files

def timing(func):
    print(timeit.timeit(func, number=1))


def run():
    book = corpus_files("ES")
    a = SpanishAnalyser(book)
    print(a.unique_lemma_freq_list[:100])
    print("Unique lemmas:", a.unique_lemmas, "Total words:", a.total_words)
    print("Words only happening once:", len((a.n_freq_lemmas(1))))
    print("coverage of 100 words:", a.word_coverage(100))
