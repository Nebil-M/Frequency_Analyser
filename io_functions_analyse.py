from analyse import *
import timeit
import pickle
import re
import os
import matplotlib.pyplot as plt
import numpy as np


# This file contains various function which though not required, are very helpful when using this program.


# Displays a graph of Percent Coverage vs Unique Lemmas of all Analyser objects inputted.
# the smaller the steps the more accurate the graph
def graph(*objs, step=100, title=None, log=True):
    fig, ax = plt.subplots()

    ax.set_xscale("log") if log else None
    ax.set_xlabel('Unique Lemmas', fontsize=12)
    ax.set_ylabel('Percent Coverage', fontsize=12)
    ax.set_title(title, fontsize=20)
    ax.grid(True)

    for obj in objs:
        x = np.arange(0, obj.unique_lemmas, step)
        y = list(map(lambda i: obj.word_coverage(i)[1], x))
        ax.plot(x, y, label=str(type(obj).__name__)[-9::-1][::-1])
    ax.legend()
    plt.show()


# A function to time other functions.
def timing(func):
    print(timeit.timeit(func, number=1))


# given a file, return the text as string. Analyser objects only take strings.
def open_book(file_dir):
    with open(file_dir, 'r', encoding="utf-8") as file:
        text = file.read()
    return text


# Given a folder, return all texts within the files and subfiles as a single string
def all_text(file_path, text=''):
    text = ''
    for file in os.scandir(file_path):
        if file.is_dir():
            text += all_text(file, text)
        else:
            with open(file, 'r', encoding="utf-8") as txt:
                text += txt.read() + '\n'
    return text


# Save an analyser object to loaded later to save time.
def save(name, obj, path):
    with open(f'{path}{name}.pkl', "wb") as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


# Given the name of the Analyser object, analyses all files in the given folder and saves them in the given destination.
def save_all(cls, folder_path, destination):
    des_name = os.path.basename(folder_path)
    des = destination + des_name + '/'
    os.mkdir(des)
    for folder in os.scandir(folder_path):
        text = all_text(folder)
        obj = cls(text)
        obj.analyse()
        save(folder.name, obj, des)


# Loads all analyser objects in given folder and running a given function on them.
def all_load_map(func, folder_path, pass_file=False, max_depth=9999, depth=1):
    for file in os.scandir(folder_path):
        if file.is_dir() and depth <= max_depth:
            depth += 1
            all_load_map(func, file, pass_file, max_depth, depth)
        else:
            obj = load_path(file)
            func(obj, file) if pass_file else func(obj)


# Returns analyser object given a pickle file.
def load_path(path):
    with open(path, "rb") as in_put:
        obj = pickle.load(in_put)
    return obj


# Loads all analyser objects in a folder. Merges them and returns one object.
def load_corpus(path):
    base_analyser = Analyser('')
    for file in os.scandir(path):
        with open(file, "rb") as in_put:
            obj = pickle.load(in_put)
            base_analyser += obj
    return base_analyser


# Trimming Gutenberg Additions:
# The following functions are only to be used on text from gutenberg. text from there have english text at the beginning
# and at the end that need to be deleted before analysis. If check is True file names of unsuccesfull trims are ouputed.

# returns trimmed text
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


# Trims the gutenberg text at the beginning of the file
def trim1(text):
    starts = re.compile(
        r"(?:The Project Gutenberg eBook|Project Gutenberg).{1,2000}\*\*\*\s?START OF (?:THE|THIS) PROJECT GUTENBERG EBOOK",
        flags=re.DOTALL | re.IGNORECASE)

    text = starts.sub('', text)

    return text


# Trims the gutenberg text at the end of the file
def trim2(text):
    endings = re.compile(r"\*\*\*\s?END OF (?:THE|THIS) PROJECT GUTENBERG EBOOK.+\*\*\*(?:[\n]|.)+",
                         flags=re.IGNORECASE)

    text = endings.sub('', text)
    return text


# Trims a whole folder and overwrites the files if overwrite is True.
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
