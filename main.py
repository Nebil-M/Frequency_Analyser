from analyse import*
import os

def process_file(lang):
  for textfile in os.scandir(f"Texts/{lang}"):
    yield textfile
    
def main():
    with open("Texts/Eng/test.txt", encoding='utf-8') as file_object:
        book = file_object.read()
    a = EnglishAnalyser(book)
    # print(a.unique_lemma_freq_list[:])
    print(a.unique_lemmas, a.total_words)
    print(len((a.n_freq_lemmas(10,10))))


if __name__ == "__main__":
    #main()
    for file in process_file("Eng"):
      with open(file, 'r', encoding="utf-8") as file_object:
        b = file_object.read()
