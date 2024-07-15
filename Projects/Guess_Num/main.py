import random


def GuessTheNum():
    random_num = random.randint(1, 100)
    amount_guess = 1

    while True:
        num_guessed = int(input("Guess a number between 1-100 !\n"))

        if num_guessed == random_num:
            print("Congrats you won !")
            break
        elif num_guessed > random_num:
            print("Lower !")
        elif num_guessed < random_num:
            print("Higher !")

        amount_guess = amount_guess + 1
    print(f"You guessed {amount_guess} times !")



def main():
    GuessTheNum()



if __name__ == "__main__":
    main()