from analyse import *
from io_functions_analyse import load, timing


def main():
    index = 12
    a = load("ES")
    coverage = 13376
    print(a.unique_lemma_freq_list[:10])
    print("Unique lemmas:", a.unique_lemmas, "Total words:", a.total_words)
    print(f"coverage of {coverage} words:", a.word_coverage(coverage))
    print("Words only happening once:", len((a.n_freq_lemmas(1))))
    print(a.n_freq_lemmas(index,index-1)[:10])
    print(a.percentage_to_required_lemmas(98))


if __name__ == "__main__":
    timing(main)

