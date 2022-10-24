import re
import spacy
from collections import Counter


class Analyser:
    def __init__(self, txt: str):
        self.txt = txt.lower()
        self.original_text = txt

        self.remove_punctuation()
        self.remove_number()

        self.word_list = self.lemmatize_txt()
        self.freq = Counter(self.word_list)
        self.unique_lemmas = len(self.freq.keys())
        self.total_words = self.freq.total()

        self.unique_lemma_freq_list = sorted(self.freq.items(), key=lambda item: item[1], reverse=True)
        self.unique_lemma_list = [i[0] for i in self.unique_lemma_freq_list]

    def __str__(self):
        return self.txt

    def remove_punctuation(self, replacement=" "):
        punctuation = re.compile(r"[!\"#$%&()*+,\-—./:;<=>?@[\\\]^_`{|}~”“¿…]+", re.IGNORECASE)
        self.txt = punctuation.sub(replacement, self.txt)

    def remove_number(self):
        n = re.compile(r"\d+", re.IGNORECASE)
        self.txt = n.sub('', self.txt)

    def n_common_words(self, n):
        return self.freq.most_common(n)

    def word_coverage(self, coverage: int):
        coverage_words = self.n_common_words(coverage)
        number_coverage_words = sum([word_freq[1] for word_freq in coverage_words])
        coverage_percentage = (number_coverage_words / self.total_words) * 100
        return number_coverage_words, coverage_percentage

    def n_freq_lemmas(self, upper, lower=0):
        return [i for i in self.unique_lemma_freq_list if lower <= i[1] <= upper]


class EnglishAnalyser(Analyser):
    def __init__(self, txt: str):
        super().__init__(txt)

    def lemmatize_txt(self):
        nlp = spacy.load("en_core_web_sm")
        for doc in nlp.pipe([self.txt], disable=["parser", "ner"]):
            yield_lemma_list = [token.lemma_.strip() for token in doc]
        lemma_list = [i for i in yield_lemma_list if i and i != '\'s']
        return lemma_list


class FrenchAnalyser(Analyser):
    def __init__(self, txt: str):
        super().__init__(txt)

    def lemmatize_txt(self):
        nlp = spacy.load("fr_core_news_sm")
        for doc in nlp.pipe([self.txt], disable=["parser", "ner"]):
            yield_lemma_list = [token.lemma_.strip() for token in doc]
        lemma_list = [i for i in yield_lemma_list if i and i != '\'s']
        return lemma_list


class SpanishAnalyser(Analyser):
    def __init__(self, txt: str):
        super().__init__(txt)

    def lemmatize_txt(self):
        nlp = spacy.load("es_core_news_sm")
        for doc in nlp.pipe([self.txt], disable=["parser", "ner"]):
            yield_lemma_list = [token.lemma_.strip() for token in doc]
        lemma_list = [i for i in yield_lemma_list if i and i != '\'s']
        return lemma_list
