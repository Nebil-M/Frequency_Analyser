from analyse import *
import timeit

def lemmatize_txt():
    with open(f"Texts/Eng/test1.txt", encoding='utf-8') as file_object:
        book = file_object.read()
    print("F",len(book))
    nlp = spacy.load("en_core_web_sm")
    lemma_list = []
    for doc in nlp.pipe(book.split('.'), disable=["parser", "ner"]):
        for token in doc:
            lemma_list.append(token.lemma_.strip())
    return lemma_list

def lemmatize_txt1():
    with open(f"Texts/Eng/test1.txt", encoding='utf-8') as file_object:
        book = file_object.read()
    print("S",len(book))
    nlp = spacy.load("en_core_web_sm")
    for doc in nlp.pipe([book], disable=["parser", "ner"]):
        yield_lemma_list = [token.lemma_.strip() for token in doc]
    lemma_list = [i for i in yield_lemma_list]
    return lemma_list


print(timeit.timeit(lemmatize_txt, number=1))
print(lemmatize_txt())
print(timeit.timeit(lemmatize_txt1, number=1))
print(lemmatize_txt1())