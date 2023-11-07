welcome_text = input("Bem vindo, deseja reservar uma mesa?\n->")
reservas = 0
numero_mesas_restaurante = 50
mesas_4 = 20
mesas_2 = 20
mesas_8 = 10

mesas_disponiveis = numero_mesas_restaurante - reservas


if welcome_text == "sim":
    print(f"Sim senhor, nós temos {mesas_disponiveis} mesas disponíveis.")
    reserva_pessoas = int(input(f"Para quantas pessoas é a reserva? "))
    if reserva_pessoas >=5 : 
        print(f"Okey, de momento temos {mesas_8} disponíveis")
        nome_cliente = input("Em que nome fica a reserva?\n->")
        hora_reserva = input(f"Okey, então fica no nome de {nome_cliente} e para que horas deseja esta reserva?\n-> ")
        print(f"Muito bem, então uma reserva para {reserva_pessoas} pessoas, em nome de {nome_cliente}, ás {hora_reserva}. ")
    elif reserva_pessoas >5:
        print(f"Temos {mesas_2}+{mesas_4} disponíveis")
        













