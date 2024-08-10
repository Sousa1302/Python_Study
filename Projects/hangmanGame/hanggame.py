import random
import string

print("Welcome to the HangMan Game !\n")

list_random_words = ["Apple", "Banana", "Orange", "Mango",
                      "Grape", "Pineapple", "Strawberry", 
                      "Watermelon", "Peach", "Cherry", "Brazil", 
                      "Canada", "France", "Japan",
                      "Australia", "India", "Germany",
                        "Mexico", "Egypt", "Italy"]

guess_wrong_letters = []
guess_correct_letters = [] 

correct_letters = []

word = random.choice(list_random_words)

for x in word:
    correct_letters.append(x)
    


def GuessTheWord():
    while True:

        print("_ " * len(word))
        print()

        guess = input("Guess a letter: ")
        if len(guess) > 0 and len(guess) < 2:
            for x in range(0, len(correct_letters)):
                if guess == correct_letters[x]:
                    
                    #print(f"{guess} is correct !\n")
                    guess_correct_letters.append(guess)
                elif guess != correct_letters[x]:
                    #print(f"{guess} is incorrect !\n")
                    guess_wrong_letters.append(guess)


            

def main():
    GuessTheWord()


if __name__ == "__main__":
    main()
