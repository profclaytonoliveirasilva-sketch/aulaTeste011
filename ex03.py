numero = int(input("Número: "))
print("1 - Par ou ímpar")
print("2 - Verificar o múltiplo de 5")
print("3 - Verificar se é maior ou menor ou igual a 10")

op = input("Escolha uma opção: ")

match op:
    case "1":
        print("1 - Par ou ímpar")
        if numero %2==0:
            print(f"{numero} é par.")
        else:
            print(f"{numero} é ímpar.")
    case "2":
        print("2 - Múltiplo de 5")
        if numero %5==0:
            print(f"{numero} é múltiplo de 5.")
        else:
            print(f"{numero} não é múltiplo de 5.")
    case "3":
        print("3 - Comparar número")
        if numero > 10:
            print(f"{numero} é maior que 10.")
        elif numero < 10:
            print(f"{numero} é menor que 10.")
        else:
            print(f"{numero} é igual a 10.")
    case _:
        print("Opção Inválida")