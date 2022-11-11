from analyse import*
import os

def corpus_files(lang):
    corpus = ""
    for textfile in os.scandir(f"Texts/{lang}"):
        with open(textfile, 'r', encoding="utf-8") as file:
            text = file.read()
        corpus += text 
    return corpus

  
def main():
    book = corpus_files("Eng")
    a = EnglishAnalyser(book)
    print(a.unique_lemma_freq_list[:100])
    print(a.unique_lemmas, a.total_words)
    print(len((a.n_freq_lemmas(1))))
    print(a.word_coverage(2553))


if __name__ == "__main__":
    main()
     
      
