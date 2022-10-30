from analyse import*


def main():
    with open("Texts/ES/test.txt", encoding='utf-8') as file_object:
        book = file_object.read()
    a = SpanishAnalyser(book)
    print(a.unique_lemma_freq_list[:])
    print(a.unique_lemmas, a.total_words)
    print(len((a.n_freq_lemmas(10,10))))


if __name__ == "__main__":
    main()
