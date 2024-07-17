import random
import string

def generator():
    size_password = int(input("Whats the size of password: "))
    print("What type of password do you wish to generate ?")
    type_pass = int(input("1. Letters \n2. Numbers \n3. Symbols \n4. Mix of all \n"))

    if type_pass == 1:
        characters = string.ascii_letters
    elif type_pass == 2:
        characters = string.digits
    elif type_pass == 3:
        characters = string.punctuation
    elif type_pass == 4:
        characters = string.printable
    else:
        print("Invalid Option !\n")

    password_generated = ''.join(random.choices(characters, k = size_password))
    print(f"Your passwor: {password_generated}")


def main():
    generator()


if __name__ == "__main__":
    main()