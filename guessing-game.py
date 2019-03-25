# guessing-game.py
# Create a program that prompts a user to guess the name of an animal.

def main():
    animal = "lion"
    print("Thinking of an animal")
    print("Guess what animal I am thinking of")
    animalguess = "incorrect"
    while animalguess == "incorrect":
        animalguess = str.lower(input())
        if animalguess == animal:
            print("Congratulations, you win!")
            print("Do you like this animal? (y/n)")
            animalaproval = input()
            if animalaproval == "y":
                print("Good for you")
            elif animalaproval == "n":
                print("That's disapointing")
            animalguess = "correct"
        elif animalguess[0] == "q":
            animalguess = "quit"
        else:
            print("Incorrect, try again")
            print("Type something that starts with the letter q to exit")
            animalguess = "incorrect"

main()
