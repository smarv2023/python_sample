import sqlite3

# Connection command and create a table
connection = sqlite3.connect("marvinsoro.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Survey(id INTEGER PRIMARY KEY, choice TEXT, count INTEGER)")

connection.commit()
cursor.close()
# Always close the connection
connection.close()


# This will add the selected color to the database
# I added tha count Integer to hold the count of the survey
def addto_Data(ID, choice, count):
    connection = sqlite3.connect("marvinsoro.db")
    cursor = connection.cursor()

    cursor.execute("INSERT OR IGNORE INTO Survey(id, choice, count) VALUES (?,?,?)", (ID, choice, count,))

    connection.commit()
    cursor.close()
    connection.close()


# This will connect to database again and Increment every time the color is selected
def increment_counter(ID):
    connection = sqlite3.connect('marvinsoro.db')
    cursor = connection.cursor()

    cursor.execute("UPDATE Survey SET count=count +1 WHERE id=?", ID)
    # Commit the changes and close the connection
    connection.commit()
    # I do not need to commit on this. This is just to view the data and put it on my prompt
    cursor.execute("SELECT * FROM Survey WHERE id=?", ID)
    update = cursor.fetchone()
    print(f"You selected {update[1]} count updated to {update[2]}")
    cursor.close()
    connection.close()


selectColors = bool
# Just an Introduction
print("This is a color survey that will record every participant's data count.")

# User will be asked if they want to submit their favorite color
# If userYorN = Y and bool is true this will go to While loop selectColors
# If userYorN = N and bool is true this will show past results and terminate the program
userYorN = input("Do you want to submit your favorite color?\n Enter:(Y)es or (N)o\n").upper()
while userYorN != "Y" and userYorN != "N":
    print("Invalid Answer --> Please type: Y or N\n")
    userYorN = input("Do you want to submit your favorite color?\n Enter:(Y)es or (N)o\n").upper()
if userYorN == "Y":
    selectColors = True
elif userYorN == "N":
    print("Okay bye!!!")
    selectColors = False

# If Y is selected this loop to ask the color until correct KEY is selected
while selectColors:
    colorChoice = input(str("Enter the number corresponding to the color:\n"
                            " 1 - Black\n 2 - White\n 3 - Red\n"
                            " 4 - Blue\n 5 - Green\n 9 - Quit\n"))

    # This will validate if the correct Key is entered
    # If the Key is valid not this will loop back
    while colorChoice != "1" and colorChoice != "2" and colorChoice != "3" and colorChoice != "4" and colorChoice != "5" and colorChoice != "9":
        print("Invalid Answer --> Choose from  1 to 5 and 9 to Quit\n")
        colorChoice = input(str("Enter the number corresponding to the color:\n"
                                " 1 - Black\n 2 - White\n 3 - Red\n"
                                " 4 - Blue\n 5 - Green\n 9 - Quit\n"))

    # If Key is correct this will give its value to the entered Key
    if colorChoice == "1":
        ID = "1"
        choice = "1 - Black"
        addto_Data(ID, choice, 0)
        increment_counter(ID)
    elif colorChoice == "2":
        ID = "2"
        choice = "2 - White"
        addto_Data(ID, choice, 0)
        increment_counter(ID)
    elif colorChoice == "3":
        ID = "3"
        choice = "3 - Red"
        addto_Data(ID, choice, 0)
        increment_counter(ID)
    elif colorChoice == "4":
        ID = "4"
        choice = "4 - Blue"
        addto_Data(ID, choice, 0)
        increment_counter(ID)
    elif colorChoice == "5":
        ID = "5"
        choice = "5 - Green"
        addto_Data(ID, choice, 0)
        increment_counter(ID)
    elif colorChoice == "9":
        print("Thank you\n Results:")
        break

    # This will ask again if you like to continue
    userYorN = input("Do you want to continue?\n Enter:(Y)es or (N)o\n").upper()
    while userYorN != "Y" and userYorN != "N":
        print("Invalid Answer --> Please type: Y or N\n")
        userYorN = input("Do you want to continue?\n Enter:(Y)es or (N)o\n").upper()
    if userYorN == "Y":
        selectColors = True
    elif userYorN == "N":
        print("Thank you\n Results:")
        selectColors = False

# To view the database
connection = sqlite3.connect("marvinsoro.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM Survey")  # execute our sql statement
results = cursor.fetchall()  # store all rows in a variable

for result in results:
    print(f"{result[1]}: {result[2]}")
cursor.close()
connection.close()
