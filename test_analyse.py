from analyse import *
from collections import Counter
from io_functions_analyse import *


def main():
    ...

def print_non_words(a):
    for w in a.unique_lemma_freq_list:
        if not w[0]:
            print(w)

def print_non_alpha(a):
    print('i for i in a.unique_lemma_freq_list if i[0].isalpha() == False')
    non_num = [i for i in a.unique_lemma_freq_list if i[0].isalpha() == False]
    print(non_num)
    print(a.unique_lemmas, a.total_words)
    # print(a.unique_lemma_freq_list)


def print_contractions(a):
    print('i for i in a.txt.split() if i.isalpha() == False')
    non_num = [i for i in a.txt.split() if i.isalpha() == False]
    print(Counter(non_num))


def print_punct(a):
    print('i for i in a.txt if i.isalpha() == False')
    non_num = [i for i in a.txt if i.isalpha() == False]
    print(Counter(non_num))

def check_unique_non_alpha(s):
    for i in s:
        if i.isalpha():
            return True
    return False

def print_unique_non_alpha(a):
    a.remove_number()
    b = set([w for w in a.txt.split() if not check_unique_non_alpha(w)])
    print(b)


if __name__ == "__main__":
    main()
    # print(len(corpus_files("Eng").split()))
    # print(len(corpus_files("ES").split()))
    # print(len(corpus_files("FR").split()))
