temp = float(input("Type a temperature: "))
whattemp = input("You want to convert to \nA. Celsius  or  B. Fahrenheit\n")

def celsius_to_fahrenheit(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    print(f"That is equal to {fahrenheit} degrees fahrenheit!\n")

def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    print(f"That is equal to {celsius} degrees celsius!\n")

def main():

    if whattemp == 'a' or whattemp == 'A':
        fahrenheit_to_celsius(temp)

    elif whattemp == 'b' or whattemp == 'B':
        celsius_to_fahrenheit(temp)


if __name__ == "__main__":
    main() 








