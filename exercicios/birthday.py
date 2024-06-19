# Evitando erros de tipo com a função str()
# se eu colocasse apenas 'age' na 'message' daria um erro pq python não sabe se quero mostrar o valor 23 ou os caracteres 2 e 3
# para evitar isso é necessário usar a função str() envolvendo a variável 'age', isso informa ao python que quero converter
# o valor 23 em uma string e exibir os caracteres 2 e 3 como parte da mensagem.

age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)