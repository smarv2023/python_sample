from basicmodule import formatToDollars

# boolean variable
convert = bool

# This will ask the user if they want to format the price
userInput = input(str("Do you want to format the price?\n (Y)es or (N)o\n")).upper()
# This will loop back if the answer is not valid
while userInput != "Y" and userInput != "N":
    print("Invalid")
    userInput = input(str("Do you want to format the price?\n Please enter: (Y)es or (N)o\n")).upper()

    if userInput == "Y":
        convert = True

    elif userInput == "N":
        print("Okay bye!")
        convert = False

# This will validate if number is entered, if not this will loop back
while convert:
    try:
        num = input("Please enter price: ")
        num = float(num)
    except ValueError:
        print("Sorry %s is not a price" % num)
        # print(f"Sorry {num} is not a number")
        continue
    else:
        print("Thank you")
        # This will break the loop if valid input is received
        break

# This is the function that was called from module "basicmoduleimport"
# This function will convert the price
formatToDollars(num)
