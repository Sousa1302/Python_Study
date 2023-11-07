number = 8
guess = 0
guess_limit = 3
while guess < guess_limit:
    guess_1 = int(input("Guess: "))
    guess += 1
    if guess_1 == number:
        print("You got it right, congrats!")
        break

else:
    print("Try again!")








