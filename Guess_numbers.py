print("\t\t\t\tDEVELOP BY MUHAMMAD SAMEER\n")
import random
number = random.randrange(1,5000)
no_of_guesses = 1
print("You have only 5 Lives")
while(no_of_guesses<=5):
    guess_number = int(input("Enter Guess Number: "))
    if guess_number > number:
        print("Enter the Lowest Number")
    elif guess_number< number:
        print("Enter High Number: ")
    else:
        print("YOU WON!!")
        print(no_of_guesses, "number of guesses he took to finish")
        break
    print(5-no_of_guesses,"lives left")
    no_of_guesses = no_of_guesses + 1
if(no_of_guesses > 5):
    print("GAME OVER!!!")
a = input()
print(a)
