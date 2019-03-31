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
            # What about asking about the animal?
            animalguess = "correct"
            break
        elif animalguess[0] == "q":
            break
        else:
            print("Incorrect, try again")
            print("Type 'end' to exit")
            animalguess = "incorrect"

main()
