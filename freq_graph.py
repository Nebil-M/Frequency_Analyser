from io_functions_analyse import*


f = load_corpus('project_data/Analyser_Objects/Eng')
e = load_corpus('project_data/Analyser_Objects/FR')
en = load_corpus('project_data/Analyser_Objects/ES')



timing(lambda: graph(f, e, en, step=1, title="Percent coverage vs Unique lemmas", log=False))

