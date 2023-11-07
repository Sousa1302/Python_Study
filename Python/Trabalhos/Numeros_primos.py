import math

# Solicita ao usuário que insira um número
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é maior que 1
if numero > 1:
    # Inicializa a variável para indicar se o número é primo
    eh_primo = True
    
    # Loop para verificar se o número é divisível por algum número entre 2 e a raiz quadrada do número
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            eh_primo = False
            break
    
    # Exibe o resultado
    if eh_primo:
        print(numero, "é um número primo.")
    else:
        print(numero, "não é um número primo.")
else:
    print("Por favor, insira um número maior que 1.")
