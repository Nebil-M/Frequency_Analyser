from analyse import *
import timeit


def timing(func):
    print(timeit.timeit(func, number=1))


with open('Texts/ES/testb.txt', 'r', encoding="utf-8") as file:
    text = file.read()

a = SpanishAnalyser(text)
print(a.unique_lemma_freq_list[:100])
print("Unique lemmas:", a.unique_lemmas, "Total words:", a.total_words)
print("Words only happening once:", len((a.n_freq_lemmas(1))))
print("coverage of 100 words:", a.word_coverage(100))
