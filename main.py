from analyse import *
from io_functions_analyse import timing, load

def main():

    a = load("FR")
    coverage = 20000
    print(a.unique_lemma_freq_list[:100])
    print("Unique lemmas:", a.unique_lemmas, "Total words:", a.total_words)
    print(f"coverage of {coverage} words:", a.word_coverage(coverage))
    print("Words only happening once:", len((a.n_freq_lemmas(1))))
    print(a.n_freq_lemmas(2,1)[:100])


if __name__ == "__main__":
    timing(main)

