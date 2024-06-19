#Todas as funções: Pensa em algo que você poderia armazenar em uma
#lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
#cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que
#crie uma lista contendo esses itens e então utilize cada função apresentada
#neste capítulo pelo menos uma vez.

lista = ['monte everest', 'pico da neblina', 'monte roraima', 'rio capibaribe', 'rio beberibe', 'brasil', 
'estados unidos', 'recife', 'olinda', 'jaboatao','portugues', 'ingles', 'alemao', 'espanhol', 'frances', 
'italiano', 'japones', 'russo']

print("Lista original:")
print(lista)

print("\n")

#del

del lista[2]
print(lista)

print("\n")

#append()

lista.append('chines')
print(lista)

print("\n")

#pop()

popped_item = lista.pop(12)
print(popped_item)
print(lista)

print("\n")

#insert()

lista.insert(5, 'portugal')
print(lista)

print("\n")

#sorted()

print(sorted(lista))

print("\n")

print(sorted(lista, reverse = True))

print("\n")

#reverse()

lista.reverse()
print(lista)

print("\n")

lista.reverse()
print(lista)

print("\n")

#sort()

lista.sort()
print(lista)

print("\n")

lista.sort(reverse = True)
print(lista)

print("\n")

#len()

print(len(lista))