from analyse import *
import timeit
import pickle
import re
import os


def open_book(file_dir):
    with open(file_dir, 'r', encoding="utf-8") as file:
        text = file.read()
    return text


def timing(func):
    print(timeit.timeit(func, number=1))


def file_text(file_path):
    corpus = ""
    for textfile in os.scandir(file_path):
        with open(textfile, 'r', encoding="utf-8") as file:
            text = file.read()
        corpus += text
    return corpus


def all_text(file_path, text=''):
    text = ''
    for file in os.scandir(file_path):
        if file.is_dir():
            text += all_text(file, text)
        else:
            with open(file, 'r', encoding="utf-8") as txt:
                text += txt.read()
    return text


def save(name, obj, path='Data/Analyse_objs/'):
    with open(f'{path}{name}.pkl', "wb") as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


def load(name, path='Data/Analyse_objs/'):
    with open(f'{path}{name}.pkl', "rb") as in_put:
        obj = pickle.load(in_put)
    return obj


def save_corpus(file_path, name, lang, path='Data/Analyse_objs'):
    book = file_text(file_path)
    if lang == 'FR':
        obj = FrenchAnalyser(book)
    elif lang == 'Eng':
        obj = EnglishAnalyser(book)
    elif lang == 'ES':
        obj = SpanishAnalyser(book)
    save(name, obj, path)


def load_path(path):
    with open(f'{path}', "rb") as in_put:
        obj = pickle.load(in_put)
    return obj


def load_corpus(name, path='Data/Analyse_objs/'):
    base_analyser = Analyser('')
    file_path = f'{path}/{name}'
    for file in os.scandir(file_path):
        with open(file, "rb") as in_put:
            obj = pickle.load(in_put)
            base_analyser += obj
    return base_analyser


# Trimming Gutenberg Additions:
def trim(text, check=False):
    original = text
    starts = re.compile(
        r"(?:The Project Gutenberg eBook|Project Gutenberg).{1,2000}\*\*\*\s?START OF (?:THE|THIS) PROJECT GUTENBERG EBOOK",
        flags=re.DOTALL | re.IGNORECASE)
    endings = re.compile(r"\*\*\*\s?END OF (?:THE|THIS) PROJECT GUTENBERG EBOOK.+\*\*\*(?:[\n]|.)+",
                         flags=re.IGNORECASE)

    text = starts.sub('', text)
    text = endings.sub('', text)

    # checking if trimming was successful
    if check:
        if starts.sub('', original) == original:
            print('First trim has failed')

        else:
            print('First trim successful')

        if endings.sub('', original) == original:
            print('Second trim has failed')
        else:
            print('Second trim successful')

        if text == original:
            print('Nothing has been trimmed')

    return text


def trim1(text):
    starts = re.compile(
        r"(?:The Project Gutenberg eBook|Project Gutenberg).{1,2000}\*\*\*\s?START OF (?:THE|THIS) PROJECT GUTENBERG EBOOK",
        flags=re.DOTALL | re.IGNORECASE)

    text = starts.sub('', text)

    return text


def trim2(text):
    endings = re.compile(r"\*\*\*\s?END OF (?:THE|THIS) PROJECT GUTENBERG EBOOK.+\*\*\*(?:[\n]|.)+",
                         flags=re.IGNORECASE)

    text = endings.sub('', text)
    return text


def trim_file(file_path, overwrite=False):
    trimmed_corp = ''
    for textfile in os.scandir(file_path):
        with open(textfile, 'r', encoding="utf-8") as file:
            txt = file.read()
            t_txt = trim(txt)
            if txt == trim1(txt):
                print(file.name, "---has failed first trim")
            if txt == trim2(txt):
                print(file.name, "---has failed second trim")
            if txt == t_txt:
                print(file.name, '---Nothing has been trimmed')
        if overwrite:
            with open(textfile, 'w', encoding="utf-8") as file:
                file.write(t_txt)

        trimmed_corp += t_txt

    return trimmed_corp
