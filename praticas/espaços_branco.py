#Acrescentando espaços em branco em strings com tabulações ou quebras de linha

#Espaços se \t
print("Python")
print("\tPython")

#QUebras de linha com \n
print("Languages: \nPython\nC\nJavaScript")

#Pode-se combinar tabulações e quebras de linha em uma única string \n\t.
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#Remover espaços em branco
#Removendo espaços em branco do lado direito de uma string usa-se o método .rstrip()
favorite_language = " python "
favorite_language = favorite_language.rstrip()

#Para remover do lado esquerdo de usa o método .lstrip()
favorite_language = favorite_language.lstrip()

#Para remover de ambos os lados ao mesmo tempo se usa .strip()
favorite_language = favorite_language.strip()