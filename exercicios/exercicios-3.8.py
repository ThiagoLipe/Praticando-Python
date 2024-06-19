#Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que
#você gostaria de visitar.

#Armazene as localidades em uma lista. Certifique-se de que a lista não esteja
#em ordem alfabética.

lugares_visitar = ['los angeles', 'israel', 'normandia', 'alemanha', 'londres']

#Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma
#elegante; basta exibi-la como uma lista Python pura.

print(lugares_visitar)

#Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a
#lista propriamente dita.

print(sorted(lugares_visitar))

#Mostre que sua lista manteve sua ordem original exibindo-a.

print(lugares_visitar)

#Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar
#a ordem da lista original.

print(sorted(lugares_visitar, reverse = True))

#Mostre que sua lista manteve sua ordem original exibindo-a.

print(lugares_visitar)

#Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar
#que sua ordem mudou.

lugares_visitar.reverse()
print(lugares_visitar)

#Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista
#para mostrar que ela voltou à sua ordem original.

lugares_visitar.reverse()
print(lugares_visitar)

#Utilize sort() para mudar sua lista de modo que ela seja armazenada em
#ordem alfabética. Exiba a lista para mostrar que sua ordem mudou.

lugares_visitar.sort()
print(lugares_visitar)

#Utilize sort() para mudar sua lista de modo que ela seja armazenada em
#ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou.

lugares_visitar.sort(reverse = True)
print(lugares_visitar)

#use len() para exibir uma mensagem informando o número de lugares na lista.
print(len(lugares_visitar))