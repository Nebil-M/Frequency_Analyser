from analyse import *
import timeit
import pickle
import re
import os


def timing(func):
    print(timeit.timeit(func, number=1))


def corpus_files(lang):
    corpus = ""
    for textfile in os.scandir(f"Texts/{lang}/Corpus"):
        with open(textfile, 'r', encoding="utf-8") as file:
            text = file.read()
        corpus += text
    return corpus


def save(name, obj):
    with open(f'{name}.pkl', "wb") as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def load(lang):
    with open(f'{lang}.pkl', "rb") as intput:
        obj = pickle.load(intput)
    return obj


def save_corpus(lang):
    book = corpus_files(lang)
    if lang == 'FR':
        obj = FrenchAnalyser(book)
    elif lang == 'Eng':
        obj = EnglishAnalyser(book)
    elif lang == 'ES':
        obj = SpanishAnalyser(book)
    save(lang, obj)


# Trimming Gutenberg Additions:
def trim(text):
    starts = re.compile(
        r"(?:The Project Gutenberg eBook|Project Gutenberg).{1,2000}\*\*\*\s?START OF (?:THE|THIS) PROJECT GUTENBERG EBOOK",
        flags=re.DOTALL | re.IGNORECASE)
    endings = re.compile(r"\*\*\*\s?END OF (?:THE|THIS) PROJECT GUTENBERG EBOOK.+\*\*\*(?:[\n]|.)+")

    text = starts.sub('', text)
    text = endings.sub('', text)
    return text


def trim1(text):
    starts = re.compile(
        r"(?:The Project Gutenberg eBook|Project Gutenberg).{1,2000}\*\*\*\s?START OF (?:THE|THIS) PROJECT GUTENBERG EBOOK",
        flags=re.DOTALL | re.IGNORECASE)

    text = starts.sub('', text)

    return text


def trim2(text):
    endings = re.compile(r"\*\*\*\s?END OF (?:THE|THIS) PROJECT GUTENBERG EBOOK.+\*\*\*(?:[\n]|.)+")

    text = endings.sub('', text)
    return text


def trim_corpus(lang):
    for textfile in os.scandir(f"Texts/{lang}/Corpus"):
        with open(textfile, 'r', encoding="utf-8") as file:
            txt = file.read()
            t_txt = trim(txt)
            if txt == trim1(txt) or txt == trim2(txt):
                print(file.name)

        with open(textfile, 'w', encoding="utf-8") as file:
            file.write(t_txt)
