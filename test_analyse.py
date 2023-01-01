from analyse import *
from collections import Counter
from io_functions_analyse import *


def main():
    name = 'Eng/18 eng'
    print_non_aplha(name)
    print_punct(name)
    #print_contractions(name)


def print_non_aplha(name):
    print('i for i in a.unique_lemma_freq_list if i[0].isalpha() == False')
    a = load(name)
    non_num = [i for i in a.unique_lemma_freq_list if i[0].isalpha() == False]
    print(non_num)
    print(a.unique_lemmas, a.total_words)
    # print(a.unique_lemma_freq_list)


def print_contractions(name):
    print('i for i in a.txt.split() if i.isalpha() == False')
    a = load(name)
    non_num = [i for i in a.txt.split() if i.isalpha() == False]
    print(Counter(non_num))


def print_punct(name):
    print('i for i in a.txt if i.isalpha() == False')
    a = load(name)
    non_num = [i for i in a.txt if i.isalpha() == False]
    print(Counter(non_num))


if __name__ == "__main__":
    main()
    # print(len(corpus_files("Eng").split()))
    # print(len(corpus_files("ES").split()))
    # print(len(corpus_files("FR").split()))
