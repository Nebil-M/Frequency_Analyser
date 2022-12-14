from analyse import *
from io_functions_analyse import load, timing, load_corpus


def main():
    index = 50
    a = load("Eng")
    coverage = 5000
    print("rare words: ", a.unique_lemma_freq_list[13000:13000 + 10])
    print("Unique lemmas:", a.unique_lemmas, "Total words:", a.total_words)
    print(f"coverage of {coverage} words:", a.word_coverage(coverage))
    print("Words only happening once:", len((a.n_freq_lemmas(1))))
    # print(a.n_freq_lemmas(index,index-1)[:10])
    print(len(a.n_freq_lemmas(index, index - 1)))
    print("Words for adequate comprehension: ", a.percentage_to_required_lemmas(98))



if __name__ == "__main__":
    # timing(main)
    e = load_corpus("Eng")
    f = load_corpus("FR")
    es = load_corpus("ES")

    print("English:")
    print(e.info())
    print("\nSpanish:")
    print(es.info())
    print("\nFrench:")
    print(f.info())
