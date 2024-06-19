# O método .sort() ordena as listas em ordem alfabéticas, depois de ordenada não se pode
# mais retornar a ordem original

carros = ['bmw', 'audi', 'toyota', 'subaru']
carros.sort()
print(carros)

# PAra uma ordem alfabética inversa usamos o argumento reverse=True dentro do .sort()
# essa alteração também é permanente
carros.sort(reverse = True)
print(carros)

# Para exibir a lista em uma ordem em particular e manter a ordem original da lista, usamos a função sorted()
# ela exibe a lista em uma ordem em particular, mas não altera a ordem propriamente da lista.

print("\nEssa é a lista original: ")
print(carros)

print("\nEssa é a lista com a função sorted(): ")
print(sorted(carros))
print("\nEssa é a lista original mais uma vez: ")
print(carros) 

# Para inverter a ordem original de uma lista, podemos usar o método reverse()
# observe que não reorganiza em ordem alfabética inversa, apenas inverte a ordem da lista
# e de maneira permanente também.
print("\nOrdem original:")
print(carros)

carros.reverse()
print("\nOrdem invertida com o .reverse():")
print(carros)

# Descobrindo o tamanho de uma lista com a função len()
print(len(carros))