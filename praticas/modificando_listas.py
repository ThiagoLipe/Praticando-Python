#Modificando elementos em uma lista

#Concatenando elementos no final de uma lista com o método .append()
motocicletas = ['honda', 'yamaha', 'suzuki', 'shineray', 'haojue']
print(motocicletas)
#motocicletas[0] = 'ducati'
#print(motocicletas)


motocicletas.append('ducati')
print(motocicletas)

#Lista vazia e então acrescentar itens à lista usando uma série
# de instruções  append()
bicicletas = []
bicicletas.append('mountain')
bicicletas.append('trial')
bicicletas.append('urbana')
print(bicicletas)

#Inserindo elementos em uma lista, pode-se adicionar um novo elemento
# em qualquer posição de sua lista usando o método  insert()
motocicletas.insert(0, 'canidale')
print(motocicletas)

#removendo elementos de uma lista com a instrução del, se souber o índice
del motocicletas[2]
print(motocicletas)

#Removendo um item com o método pop()
popped_motocicletas = motocicletas.pop()
print(motocicletas)
print(popped_motocicletas)

#Removendo itens de qualquer posição em uma lista
first_owned = motocicletas.pop(1)
print("A primeira motocicleta que tive foi uma " + first_owned.title() + ".")

#Removendo um item de acordo com o valor, remove()
print(motocicletas)
motocicletas.remove('suzuki')
print(motocicletas)

# o método  remove() para trabalhar com um valor que está sendo
# removido de uma lista. Vamos remover o valor 'ducati' e 
# exibir um motivo para removê-lo da lista
too_expensive = 'haojue'
motocicletas.remove(too_expensive)
print(motocicletas)
print("\nA " + too_expensive.title() + " é muito cara pra mim")