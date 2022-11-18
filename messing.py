from io_functions_analyse import *
from analyse import*

#save_corpus("ES")


index = 50
a = SpanishAnalyser(corpus_files("ES"))
coverage = 5000
print(a.unique_lemma_freq_list[13000:13000+10])
print("Unique lemmas:", a.unique_lemmas, "Total words:", a.total_words)
print(f"coverage of {coverage} words:", a.word_coverage(coverage))
print("Words only happening once:", len((a.n_freq_lemmas(1))))
print(a.n_freq_lemmas(index,index-1)[:10])
print(len(a.n_freq_lemmas(index,index-1)))
print("Words for adequate comprehension: ", a.percentage_to_required_lemmas(98))