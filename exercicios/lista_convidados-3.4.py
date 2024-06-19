#Se fosse convidar alguém, para jantar, quem você convidaria?
# Crie uma lista que inclua pelo menos três pessoas que você gostaria de convidar
# para jantar. Em seguida, utilize sua lista para exibir uma mensagem para cada pessoa,
# convidando-a para jantar.

convidados = ['pedro', 'marcia', 'catia']
mensagem = ", convido você para jantar, hoje á noite."
print("\n" + convidados[0].title() + mensagem)
print(convidados[1].title() + mensagem)
print(convidados[2].title() + mensagem)

#3.5 – Alterando a lista de convidados: Você acabou de saber que um 
#de seus convidados não poderá comparecer ao jantar, portanto será necessário
#enviar um novo conjunto de convites. Você deverá pensar em outra pessoa para 
#convidar.

#Comece com seu programa do Exercício 3.4. Acrescente uma instrução print 
#no final de seu programa, especificando o nome do convidado que não
#poderá comparecer.

print("\nA " + convidados[2].title() + " informou que não poderá comparecer.\n")

#Modifique sua lista, substituindo o nome do convidado que não poderá comparecer 
#pelo nome da nova pessoa que você está convidando.

convidados[2] = 'selma'
print(convidados)

#Exiba um segundo conjunto de mensagens com o convite, uma para cada pessoa que 
#continua presente em sua lista.

print("\n" + convidados[0].title() + " convido você para jantar.")
print(convidados[1].title() + " convido você para jantar.")
print(convidados[2].title() + " convido você para jantar.")

#3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior,portanto agora tem
#mais espaço disponível. Pense em mais três convidados para o jantar.
#• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente uma instrução print no final de seu programa informando às pessoas que você encontrou uma mesa de jantar maior.
#• Utilize insert() para adicionar um novo convidado no início de sua lista.
#• Utilize insert() para adicionar um novo convidado no meio de sua lista.
#• Utilize append() para adicionar um novo convidado no final de sua lista.
#Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que está em sua lista.

print("\nOlá, " + convidados[0].title() + ", " + convidados[1].title() + " e " + convidados[2].title() + ", encontrei uma mesa maior!")
convidados.insert(0, 'manuela')
convidados.insert(2,'fernando')
convidados.append('fabiola')

novo_convite = ", convido para jantar, hoje á noite!"
print("\n" + convidados[0].title() + novo_convite)
print(convidados[1].title() + novo_convite)
print(convidados[2].title() + novo_convite)
print(convidados[3].title() + novo_convite)
print(convidados[4].title() + novo_convite)
print(convidados[5].title() + novo_convite)

#3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova mesa de jantar não chegará a tempo para o jantar e tem espaço para somente dois convidados.
#• Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que mostre uma mensagem informando que você pode convidar apenas duas pessoas para o jantar.
#• Utilize pop() para remover os convidados de sua lista, um de cada vez, até que apenas dois nomes permaneçam em sua lista. Sempre que remover um nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela saiba que você sente muito por não poder convidá-la para o jantar.
#• Apresente uma mensagem para cada uma das duas pessoas que continuam na lista, permitindo que elas saibam que ainda estão convidadas.
#• Utilize del para remover os dois últimos nomes de sua lista, de modo que você tenha uma lista vazia. Mostre sua lista para garantir que você realmente tem uma lista vazia no final de seu programa.

print("\nInfelizmente, terei que convidar apenas duas pessoas da lista.\n")

cancelar_convite = ', não há espaço suficiente.'

desconvidado_1 = convidados.pop(0)
print("\n" + desconvidado_1.title() + cancelar_convite)

desconvidado_2 = convidados.pop(1)
print("\n" + desconvidado_2.title() + cancelar_convite)

desconvidado_3 = convidados.pop(2)
print("\n" + desconvidado_3.title() + cancelar_convite)

desconvidado_4 = convidados.pop(0)
print("\n" + desconvidado_4.title() + cancelar_convite + "\n")

manter_convite = ', seu convite está mantido.'

print(convidados[0].title() + manter_convite)
print(convidados[1].title() + manter_convite + "\n")

#Utilize del para remover os dois últimos nomes de sua lista, de modo que você tenha uma lista
#vazia. Mostre sua lista para garantir que você realmente tem uma lista vazia no final de seu
#programa.

del convidados[0]
del convidados[0]
print(convidados)


print(len(convidados))