from analyse import *
from collections import Counter


def main():
    with open("Texts/ES/test.txt", encoding='utf-8') as file_object:
        book = file_object.read()
    print_non_aplha_eng(book)
    print_contractions_eng(book)
    print_punct(book)


def print_non_aplha_eng(text):
    a = SpanishAnalyser(text)
    non_num = [i for i in a.unique_lemma_freq_list if i[0].isalpha() == False]
    print(non_num)
    print(a.unique_lemmas, a.total_words)


def print_contractions_eng(text):
    a = SpanishAnalyser(text)
    non_num = [i for i in a.txt.split() if i.isalpha() == False]
    print(Counter(non_num))


def print_punct(text):
    a = SpanishAnalyser(text)
    non_num = [i for i in a.txt if i.isalpha() == False]
    print(Counter(non_num))


if __name__ == "__main__":
    main()
