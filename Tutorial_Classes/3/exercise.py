nome = input("Your name: ")
idade = int(input("Your age: "))
email = input("Your email: ")

Client_Name = "So your name is %s"
CLient_Age = "And you are %d years old"
Client_Email = "Your email is %s"

print(Client_Name % (nome))
print(CLient_Age % (idade))
print(Client_Email % (email))

print(f"Hey there {nome}, so you are {idade} years old and your email is {email}")




