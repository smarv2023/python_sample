# Function to for sorting if first name or last name first
def sortName(firstname, lastname, sortorder="firstlast"):
    # If choose Last name first "lastfirst"
    if sortorder == "lastfirst" or sortorder == '2':
        if lastname == "" and firstname == "":
            print("Last, First")
        elif firstname == "":
            firstname = "(blank)"
            print("Last and First name\n", lastname + ", " + firstname)
        elif lastname == "":
            lastname = "(blank)"
            print("Last and First name\n", lastname + ", " + firstname)
        else:
            print("Last and First name\n", lastname + ", " + firstname)
    # Default and if choose first name "firstlast"
    else:
        if firstname == "" and lastname == "":
            print("First Last")
        elif firstname == "":
            firstname = "(blank)"
            print("First and Last name\n", firstname + " " + lastname)
        elif lastname == "":
            lastname = "(blank)"
            print("First and Last name\n", firstname + " " + lastname)
        else:
            print("First and Last name\n", firstname + " " + lastname)


# Input Name and select what sort
sortName(input("Enter First Name: "), input("Last Name: "),
         input("Select Order: type the number(1 or 2) or word(firstlast or lastfirst)\n 1.)firstlast\n 2.)lastfirst\n"))
