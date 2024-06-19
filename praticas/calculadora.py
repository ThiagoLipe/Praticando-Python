print("")
print("---------------  MENU  ---------------")
print("")
print("1 para SOMA")
print("2 para SUBTRAÇÃO")
print("3 para DIVISÃO")
print("4 para MULTIPLICAÇÃO")
print("")
print("--------------------------------------")
print("")
opcao = int(input("Escolha uma opção: "))
print("")

if opcao == 1:
    print("")
    print("-----------------------  SOMA  -----------------------")
    print("")
    
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro: "))
    
    print("")
    print("------------------------------------------------------")

    soma = num1 + num2

    print("")
    print(num1, "mais", num2, "é igual a:", soma)
    print("")
    print("------------------------------------------------------")

elif opcao == 2:
    print("")
    print("----------------------- SUBTRAÇÃO -----------------------")
    print("")

    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro: "))

    print("")
    print("-----------------------------------------------------------")

    subtracao = num1 - num2

    print("")
    print(num1, "menos", num2, "é igual a:", subtracao)
    print("")
    print("-----------------------------------------------------------")

elif opcao == 3:
    print("")
    print("-----------------------  DIVISÃO  -----------------------")
    print("")

    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro: "))

    print("")
    print("---------------------------------------------------------")

    divisao = num1 / num2

    print("")
    print(num1, "dividido por", num2, "é igual a:", divisao)
    print("")
    print("---------------------------------------------------------")

elif opcao == 4:
    print("")
    print("-----------------------  MULTIPLICAÇÃO  -----------------------")
    print("")

    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite outro: "))

    print("")
    print("---------------------------------------------------------------")

    mult = num1 * num2

    print("")
    print(num1, "multiplicado por", num2, "é igual a:", mult)
    print("")
    print("---------------------------------------------------------------")

else:
    print("")
    print("Opção inválida")
    print("")
    print("---------------------------------------------------------------")
