from analyse import*
import os

def corpus_files(lang):
    corpus = ""
    for textfile in os.scandir(f"Texts/{lang}/CorpusES"):
        with open(textfile, 'r', encoding="utf-8") as file:
            text = file.read()
        corpus += text 
    return corpus

  
def main():
    book = corpus_files("ES")
    a = SpanishAnalyser(book)
    print(a.unique_lemma_freq_list[:100])
    print("Unique lemmas:",a.unique_lemmas, "Total words:",a.total_words)
    print("Words only happening once:",len((a.n_freq_lemmas(1))))
    print("coverage of 100 words:",a.word_coverage(100))


if __name__ == "__main__":
    main()
     
      
