import re
from collections import Counter
import stanza


class Analyser:
    def __init__(self, txt: str = ''):
        self.txt = txt.lower()
        self.original_text = txt

        self.doc = None
        self.word_list = []
        self.freq = {}
        self.total_words = 1
        self.unique_lemmas = 0

        self.unique_lemma_freq_list = []
        self.unique_lemma_list = []

    def __str__(self):
        return self.txt

    def __add__(self, other):
        analyser = eval(type(other).__name__)
        a = analyser(self.original_text + other.original_text)
        a.txt = self.txt + other.txt
        a.reanalyse(self.word_list, other.word_list)
        return a

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

    def reanalyse(self, *word_lists):
        self.word_list = []
        for word_list in word_lists:
            self.word_list += word_list

        self.freq = Counter(self.word_list)
        self.total_words = sum(self.freq.values())
        self.unique_lemmas = len(self.freq.keys())

        self.unique_lemma_freq_list = sorted(self.freq.items(), key=lambda item: item[1], reverse=True)
        self.unique_lemma_list = [i[0] for i in self.unique_lemma_freq_list]

    def relemmatize(self):
        if self.doc:
            lemmas_list = list(map(lambda w: w.lemma if w.lemma else w.text, self.doc.iter_words()))
            return lemmas_list

    def info(self, coverage=5000):
        s = '-----------------\n'
        s += f'Unique lemmas: {self.unique_lemmas} , Total words: {self.total_words} \n'
        s += f"coverage of {coverage} words: {self.word_coverage(coverage)} \n"
        s += f"Words for adequate comprehension: {self.percentage_to_required_lemmas(98)}"
        return s

    def remove_punctuation(self, replacement=" "):
        # Remove all punctuation except Apostrophe(') as to not mess up contractions.
        punctuation = re.compile(r"[!\"#$%&()*+,\-—./:;<=>?@[\\\]^_`{|}~”“¿…«»°¡™©"
                                 r"\ufeff·×↑┤†│┌★─║⁠┘→§¤└├¶▼–¾•┐‒£┼−]+",
                                 re.IGNORECASE)
        self.txt = punctuation.sub(replacement, self.txt)

    def remove_number(self):
        n = re.compile(r"\d+", re.IGNORECASE)
        self.txt = n.sub('', self.txt)

    def lemmatize_txt(self):
        return self.txt.split()

    def word_coverage(self, coverage: int):
        coverage_words = self.unique_lemma_freq_list[0:coverage]
        number_coverage_words = sum([word_freq[1] for word_freq in coverage_words])
        coverage_percentage = (number_coverage_words / self.total_words) * 100
        return number_coverage_words, coverage_percentage

    def n_freq_lemmas(self, upper, lower=0):
        return [i for i in self.unique_lemma_freq_list if lower <= i[1] <= upper]

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


class EnglishAnalyser(Analyser):
    def __init__(self, txt: str):
        super().__init__(txt)

    def lemmatize_txt(self):
        nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma', download_method=None)
        self.doc = nlp(self.txt)
        lemmas_list = list(map(lambda w: w.lemma if w.lemma else w.text, self.doc.iter_words()))
        return lemmas_list


class FrenchAnalyser(Analyser):
    def __init__(self, txt: str):
        super().__init__(txt)

    def lemmatize_txt(self):
        nlp = stanza.Pipeline(lang='fr', processors='tokenize,mwt,pos,lemma', download_method=None)
        self.doc = nlp(self.txt)
        lemmas_list = list(map(lambda w: w.lemma if w.lemma else w.text, self.doc.iter_words()))
        return lemmas_list


class SpanishAnalyser(Analyser):
    def __init__(self, txt: str):
        super().__init__(txt)

    def lemmatize_txt(self):
        nlp = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma', download_method=None)
        self.doc = nlp(self.txt)
        lemmas_list = list(map(lambda w: w.lemma if w.lemma else w.text, self.doc.iter_words()))
        return lemmas_list
