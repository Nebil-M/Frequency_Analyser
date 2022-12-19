from io_functions_analyse import *
from analyse import*

#save_corpus("ES")



e = EnglishAnalyser(open_book("Texts/Eng/Corpus/The Time Machine by H. G. Wells.txt"))
s = SpanishAnalyser(open_book("Texts/ES/Corpus/La Navidad en las Montañas.txt"))
f = FrenchAnalyser(open_book('Texts/FR/Corpus/Madame Bovary.txt'))

#e = load('Eng')
# s = load("ES")
#f = load("FR")

def info(a):
    coverage = 5000
    print("Unique lemmas:", a.unique_lemmas, ", Total words:", a.total_words)
    print(f"coverage of {coverage} words:", a.word_coverage(coverage))
    print("Words for adequate comprehension: ", a.percentage_to_required_lemmas(98))

print("English:")
info(e)
print("\nSpanish:")
info(s)
print("\nFrench:")
info(f)