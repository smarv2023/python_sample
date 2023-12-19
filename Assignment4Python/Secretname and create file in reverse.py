# Variables
guesses = []
secretname = 'Marsor'
loadFile = []


# Function to validate the input if match the secretname
def checkNameGuesses(guesses, secretname):
    for name in guesses:
        if name == secretname:
            return True
    return False


# This is the code of the function that will reverse content and re-write the text
def reverseNamesAndWriteToFile(names):
    result = open("resultsFile.txt", "w")
    for saved in reversed(range(len(names))):
        result.write(names[saved] + "\n")
    print("File Saved!!!")
    result.close()


# Create File if not existing
file = open("resultsFile.txt", "a+")
file.close()

# This will show what is inside the resultsFile
file = open("resultsFile.txt")
for line in file:
    print(line, end="")
file.close()

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

# This will load the text file put it in the list array
with open("resultsFile.txt", "r") as file:
    myNames = [line.strip() for line in file]

# This will the text file reverse back the original order
# And turn it back to list array
for y in reversed(range(len(myNames))):
    loadFile.append(myNames[y])

# This will combine the both original order of text and new guessed
# This combination will connect the original order of data
names = loadFile + guesses

# This call function will reverse all the list and write file
reverseNamesAndWriteToFile(names)
