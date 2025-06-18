def menu():
    print("\nMenu")
    print("1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Raiz Quadrada")
    op = input("Escolha a opção de cálculo desejada:\n ")
    while (op == "") or (op != "1" and op != "2" and op != "3" and op != "4" and op != "5" and op != "6"):
        op = input("\nOpção Inválida, por favor escolha a opção de cálculo desejada:\n ")
    else:
        return op

def adição():
    print("\nModo ADIÇÃO")
    n1 = int(input("Digite o primeiro número desejado:\n"))
    n2 = int(input("Digite o segundo número desejado:\n"))
    soma = n1 + n2
    print(f"A soma de {n1} mais {n2} é igual a: {soma}")

def menos():
    print("\nModo SUBTRAÇÃO")
    n1 = int(input("Digite o primeiro número desejado: \n"))
    n2 = int(input("Digite o segundo número desejado: \n"))
    sub = n1 - n2
    print(f"A Subtração de {n1} menos {n2} é igual a: {sub}")

def multi():
    print("\nModo MULTIPLICAÇÃO")
    n1 = int(input("Digite o primeiro número desejado: \n"))
    n2 = int(input("Digite o segundo número desejado: \n"))
    vez = n1 * n2
    print(f"A multiplicação de {n1} vezes {n2} é igual a: {vez}")

def divisao():
    print("\nModo DIVISÃO")
    n1 = int(input("Digite o primeiro número desejado: \n"))
    n2 = int(input("Digite o segundo número desejado: \n"))
    div = n1/n2
    print(f"A divisão de {n1} por {n2} é igual a: {div}")

def raiz_quad():
    import math
    print("\nModo RAÍZ QUADRADA")
    n1 = int(input("Digite o número que deseja saber a raíz quadrada: \n"))
    raiz = math.sqrt(n1)
    print(f"A Raiz Quadrada do número {n1} é igual a:", raiz)

#Main
print("CALCULADORA SIMPLES")
confirma = input("Confirma a abertura da Calculadora?:\n1 - SIM\n2 - NÃO\n")
while confirma =="1":
    escolha = menu()
    if escolha == "1":
        adição()
    elif escolha == "2":
        menos()
    elif escolha == "3":
        multi()
    elif escolha == "4":
        divisao()
    elif escolha == "5":
        raiz_quad()
    else:
        print("Modo Inválido")
else:
    print("Saindo")