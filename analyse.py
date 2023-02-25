import re
from collections import Counter
import stanza

# This file contains all the analyser objects. Analysis can be done by importing classes from this file and running them
# in a different folder. Another file contains very helpful functions to make analysis easier.


# The base class used to make language specific Analyser Objects. Doesn't include lemmatization if used by itself.
class Analyser:
    def __init__(self, txt: str = ''):
        # txt is the text that will be cleaned while the other saves the text.
        self.txt = txt.lower()
        self.original_text = txt

        # initializing all variables with default values. Total words is 1 because it is used as a denominator.
        # doc is a stanza document after lemmatization is done.
        self.doc = None
        self.word_list = []
        self.freq = {}
        self.total_words = 1
        self.unique_lemmas = 0

        self.unique_lemma_freq_list = []
        self.unique_lemma_list = []

    def __str__(self):
        return self.txt

    # A way to merge Analyser objects. Some info is lost but main functionality is kept.
    def __add__(self, other):
        analyser = eval(type(other).__name__)
        a = analyser(self.original_text + other.original_text)
        a.txt = self.txt + other.txt
        a.doc = None
        a.reanalyse(self.word_list, other.word_list)
        return a

    # The main function of this program. Needs to be run after an Analyser object is created.
    def analyse(self, txt=None):
        if txt:
            self.txt = txt.lower()
            self.original_text = txt

        self.remove_punctuation()
        self.remove_number()

        self.word_list = self.lemmatize_txt()
        self.freq = Counter(self.word_list)
        self.total_words = sum(self.freq.values())
        self.unique_lemmas = len(self.freq.keys())

        self.unique_lemma_freq_list = sorted(self.freq.items(), key=lambda item: item[1], reverse=True)
        self.unique_lemma_list = [i[0] for i in self.unique_lemma_freq_list]

    # If a word_list is provided, reanalyse the data. Some info is lost.
    def reanalyse(self, *word_lists):
        self.doc = None
        self.word_list = []
        for word_list in word_lists:
            self.word_list += word_list

        self.freq = Counter(self.word_list)
        self.total_words = sum(self.freq.values())
        self.unique_lemmas = len(self.freq.keys())

        self.unique_lemma_freq_list = sorted(self.freq.items(), key=lambda item: item[1], reverse=True)
        self.unique_lemma_list = [i[0] for i in self.unique_lemma_freq_list]

    # Only done if a doc object is available after using stanza
    def relemmatize(self):
        if self.doc:
            lemmas_list = list(map(lambda w: w.lemma if w.lemma else w.text, self.doc.iter_words()))
            return lemmas_list

    # Shows the basic info provided by this program. More complex info can be accessed using the attributes and methods.
    def info(self, coverage=5000):
        s = '-----------------\n'
        s += f'Unique lemmas: {self.unique_lemmas} , Total words: {self.total_words} \n'
        s += f"coverage of {coverage} words: {self.word_coverage(coverage)} \n"
        s += f"Words for adequate comprehension: {self.percentage_to_required_lemmas(98)}"
        return s

    # called in analyse method in order to clean the text.
    def remove_punctuation(self, replacement=" "):
        # Remove all punctuation except Apostrophe(') as to not mess up contractions.
        punctuation = re.compile(r"[!\"#$%&()*+,\-—./:;<=>?@[\\\]^_`{|}~”“¿…«»°¡™©"
                                 r"\ufeff·×↑┤†│┌★─║⁠┘→§¤└├¶▼–¾•┐‒£┼−]+",
                                 re.IGNORECASE)
        self.txt = punctuation.sub(replacement, self.txt)

    # called in analyse method in order to clean the text of digits such as 0,1,2,3,4,5,6,7,8,9.
    def remove_number(self):
        n = re.compile(r"\d+", re.IGNORECASE)
        self.txt = n.sub('', self.txt)

    # The Method to be overridden by language-specific child classes. This default method just separates by text.
    def lemmatize_txt(self):
        return self.txt.split()

    # input int n, return how many words n lemmas make up and what percentage of words n lemmas make up as a tuple.
    def word_coverage(self, coverage: int):
        coverage_words = self.unique_lemma_freq_list[0:coverage]
        number_coverage_words = sum([word_freq[1] for word_freq in coverage_words])
        coverage_percentage = (number_coverage_words / self.total_words) * 100
        return number_coverage_words, coverage_percentage

    # Return lemmas that fit the constrains of a minimum and maximum frequency as inputted.
    def n_freq_lemmas(self, upper, lower=0):
        return [i for i in self.unique_lemma_freq_list if lower <= i[1] <= upper]

    # Takes a percentage and returns how many lemmas would be needed to reach that much percent coverage of the text.
    def percentage_to_required_lemmas(self, percentage):
        number_of_words = (percentage / 100) * self.total_words
        required_lemmas = 0
        sum_of_lemmas = 0
        for lemma in self.unique_lemma_freq_list:
            if number_of_words <= sum_of_lemmas:
                break
            sum_of_lemmas += lemma[1]
            required_lemmas += 1
        return required_lemmas


# Language Specific classes. Naming must be written the following format: LanguageAnalyser
class EnglishAnalyser(Analyser):
    def __init__(self, txt: str):
        super().__init__(txt)

    # A lemmatizer function specific to english.
    def lemmatize_txt(self):
        nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma', download_method=None)
        self.doc = nlp(self.txt)
        lemmas_list = list(map(lambda w: w.lemma if w.lemma else w.text, self.doc.iter_words()))
        return lemmas_list


class FrenchAnalyser(Analyser):
    def __init__(self, txt: str):
        super().__init__(txt)

    # A lemmatizer function specific to French.
    def lemmatize_txt(self):
        nlp = stanza.Pipeline(lang='fr', processors='tokenize,mwt,pos,lemma', download_method=None)
        self.doc = nlp(self.txt)
        lemmas_list = list(map(lambda w: w.lemma if w.lemma else w.text, self.doc.iter_words()))
        return lemmas_list


class SpanishAnalyser(Analyser):
    def __init__(self, txt: str):
        super().__init__(txt)

    # A lemmatizer function specific to Spanish.
    def lemmatize_txt(self):
        nlp = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma', download_method=None)
        self.doc = nlp(self.txt)
        lemmas_list = list(map(lambda w: w.lemma if w.lemma else w.text, self.doc.iter_words()))
        return lemmas_list
