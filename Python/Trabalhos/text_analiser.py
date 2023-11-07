print("Bem vindo ao analisador de texto !")
texto = input("Por favor escreva o seu texto abaixo. \n->")

n_words = len(texto)

def contar_frases(texto):
    # Remover espaços em branco extras no início e no final do texto
    texto = texto.strip()
    
    # Contadores de frases
    num_frases = 0
    
    # Caracteres que indicam o final de uma frase
    caracteres_fim_frase = ['.', '!', '?']
    
    # Percorrer o texto e contar as frases
    for caractere in texto:
        if caractere in caracteres_fim_frase:
            num_frases += 1
    
    # Retornar o número total de frases
    return num_frases


total_frases = contar_frases(texto)
print("Número de frases:", total_frases)
print(f"O texto anterior possui {n_words} palavras ")













