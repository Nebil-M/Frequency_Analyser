import re
import spacy
from collections import Counter
import stanza




class Analyser:
    def __init__(self, txt: str):
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

    def __str__(self):
        return self.txt

    def __add__(self, other):
        word_list = self.word_list + other.word_list
        return ListAnalyser(word_list)

    def info(self, coverage=5000):
        s = '-----------------\n'
        s += f'Unique lemmas: {self.unique_lemmas} , Total words: {self.total_words} \n'
        s += f"coverage of {coverage} words: {self.word_coverage(coverage)} \n"
        s += f"Words for adequate comprehension: {self.percentage_to_required_lemmas(98)}"
        return s

    def remove_punctuation(self, replacement=" "):
        # Remove all punctuation except Apostrophe(') as to not mess up contractions.
        # «·×↑\ufeff
        # │¤£×└──────┘•–––↑└───┘§¤¤¾┌───┐║‒┼£·→┌──────┐▼★†¶−−−−−−−−−├──────┤
        punctuation = re.compile(r"[!\"#$%&()*+,\-—./:;<=>?@[\\\]^_`{|}~”“¿…«»°¡™©"
                                 r"·×↑\ufeff│¤£×└──────┘•–––↑└───┘§¤¤¾┌───┐║‒┼£·→┌──────┐▼★†¶−−−−−−−−−├──────┤]+",
                                 re.IGNORECASE)
        self.txt = punctuation.sub(replacement, self.txt)

    def remove_number(self):
        n = re.compile(r"\d+", re.IGNORECASE)
        self.txt = n.sub('', self.txt)

    def lemmatize_txt(self):
        return self.txt.split()

    # Not used, get rid of later
    def n_common_words(self, n):
        return self.freq.most_common(n)

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
        nlp = spacy.load("en_core_web_sm")
        tokens = []
        for doc in nlp.pipe(self.txt.split('\n\n'), disable=["parser", "ner"]):
            tokens += list(filter(lambda token: not token.is_space, doc))
        lemma_list = list(map(lambda token: token.lemma_, tokens))

        return lemma_list


class FrenchAnalyser(Analyser):
    def __init__(self, txt: str):
        super().__init__(txt)

    def lemmatize_txt(self):
        nlp = spacy.load("fr_core_news_sm")
        tokens = []
        for doc in nlp.pipe(self.txt.split('\n\n'), disable=["parser", "ner"]):
            tokens += list(filter(lambda token: not token.is_space, doc))
        lemma_list = list(map(lambda token: token.lemma_, tokens))

        return lemma_list


class SpanishAnalyser(Analyser):
    def __init__(self, txt: str):
        super().__init__(txt)

    def lemmatize_txt(self):
        nlp = spacy.load("es_core_news_sm")
        tokens = []
        for doc in nlp.pipe(self.txt.split('\n\n'), disable=["parser", "ner"]):
            tokens += list(filter(lambda token: not token.is_space, doc))
        lemma_list = list(map(lambda token: token.lemma_, tokens))

        return lemma_list

    # Seperates el and other words but possibly wrong
    def lemmatize_txt_prefix(self):
        nlp = spacy.load("es_core_news_sm")
        lemma_list = []
        for doc in nlp.pipe(self.txt.split('\n\n'), disable=["parser", "ner"]):
            for token in doc:
                token = token.lemma_.strip().split()
                if token:
                    for i in token:
                        lemma_list.append(i)
        return lemma_list

# for adding purposes.
class ListAnalyser(Analyser):
    def __init__(self, word_list):
        self.word_list = word_list
        self.freq = Counter(self.word_list)
        self.total_words = sum(self.freq.values())
        self.unique_lemmas = len(self.freq.keys())

        self.unique_lemma_freq_list = sorted(self.freq.items(), key=lambda item: item[1], reverse=True)
        self.unique_lemma_list = [i[0] for i in self.unique_lemma_freq_list]



# Test
class FrenchAnalyser2(Analyser):
    def __init__(self, txt: str):
        super().__init__(txt)

    def lemmatize_txt(self):
        nlp = stanza.Pipeline(lang='fr', processors='tokenize,mwt,pos,lemma', download_method=None)
        doc = nlp(self.txt)
        lemmas_list = []
        for sentence in doc.sentences:
            for word in sentence.words:
                lemmas_list.append(word.lemma)
        return lemmas_list