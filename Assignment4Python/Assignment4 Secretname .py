# Variables
guesses = []
secretname = 'Marsor'


# Function to validate the input
def checkNameGuesses(guesses, secretname):
    for name in guesses:
        if name == secretname:
            return True
    return False


# This will collect the input, store it in guesses[] and give a print a result
print("Enter the secret name: ")
for x in range(5):
    guesses.append(input(x + 1))
    if checkNameGuesses(guesses, secretname):
        print(checkNameGuesses(guesses, secretname), "\nCongratulations!!!")
        break
    else:
        print(checkNameGuesses(guesses, secretname))

if not (checkNameGuesses(guesses, secretname)):
    print(guesses, "<<All are incorrect\nSorry try again")
