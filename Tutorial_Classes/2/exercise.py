# library used to generate random nums
import random   

def num_generator():
    # generates a random integer between 1 and 100
    random_num = random.randint(1,100)
    
    
    while(True):

        guess = int(input("Guess a number between 1-100: "))

        if(guess > random_num):
            print("Lower !")

        elif(guess < random_num):
            print("Higher !")

        elif(guess == random_num):
            print("Congrats you won !")
            break


def main():
    num_generator()


if __name__ == "__main__":
    main()