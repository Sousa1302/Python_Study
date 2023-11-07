import random
import string

def gerar_caracteres_aleatorios(tamanho):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

# Exemplo de uso
tamanho_desejado = 10
aleatorio = gerar_caracteres_aleatorios(tamanho_desejado)
print(aleatorio)
