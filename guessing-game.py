# guessing-game.py
# Create a program that prompts a user to guess the name of an animal.

def main():
    animal = "lion"
    print("Thinking of an animal.")
    print("Guess what animal I am thinking of.")
    animalguess = "incorrect"
    while animalguess == "incorrect":
        animalguess = input()
        if animalguess == animal:
            print("Congratulations, you win!")
            animalguess = "correct"
        else:
            print("Incorrect, try again.")
            animalguess = "incorrect"

main()
