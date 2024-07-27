import random

random_num = random.randint(1,100)

guess = 0
amount_try = 0

while random_num != guess and amount_try <= 5:
    guess = int(input("Guess a num between 1-100\n"))

    amount_try += 1
   
    if guess > random_num:
        print("Lower !\n")
    if guess < random_num:
        print("Higher !\n")
    elif guess == random_num:
        print("Congrats you Won !\n")
        break 
