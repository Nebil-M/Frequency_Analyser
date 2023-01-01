from io_functions_analyse import *
from analyse import*


a = FrenchAnalyser(all_text('Texts/FR'))

print(a.info(coverage=1000))

print(len(a.txt.split()))







