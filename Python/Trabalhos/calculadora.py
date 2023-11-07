welcome_text = input("Welcome to the calculator app! \nWhat can i help you with? ")

if welcome_text.lower() == "sum":
    num1 = float(input("What is your first number? "))
    num2 = float(input("What is your second number? "))
    print(num1 + num2)
    
if welcome_text.lower() == "sub":
    num3 = float(input("What is your first number? "))
    num4 = float(input("What is your second number? "))
    print(num3 - num4)

if welcome_text.lower() == "div":
    num5 = float(input("What is your first number?"))
    num6 = float(input("What is your second number? "))
    print(num5 / num6)

if welcome_text.lower() == "mul":
    num7 = float(input("What is your first number? "))
    num8 = float(input("What is your second number? "))
    print(num7 * num8)

else:
    print("Sorry i don't know what are you talking about!")














