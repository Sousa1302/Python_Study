def swap_variables(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# Exemplo de uso da função
x = 100
y = 200
print("Antes da troca: x =", x, "e y =", y)

x, y = swap_variables(x, y)
print("Depois da troca: x =", x, "e y =", y)
