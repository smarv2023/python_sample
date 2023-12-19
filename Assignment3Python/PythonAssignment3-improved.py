# Function to for sorting if first name or last name first
def sortName(firstname, lastname, sortorder="firstlast"):

    # Default and if choose first name "firstlast"
    if sortorder == "firstlast" or sortorder == '1' or sortorder == "":
        print("First and Last name")
        if firstname == "" and lastname == "":
            return "First Last"
        elif firstname == "":
            firstname = "(blank)"
            return firstname + " " + lastname
        elif lastname == "":
            lastname = "(blank)"
            return firstname + " " + lastname
        else:
            return firstname + " " + lastname

    # If choose Last name first "lastfirst"
    elif sortorder == "lastfirst" or sortorder == '2':
        print("Last and First name")
        if lastname == "" and firstname == "":
            return "Last, First"
        elif firstname == "":
            firstname = "(blank)"
            return lastname + ", " + firstname
        elif lastname == "":
            lastname = "(blank)"
            return lastname + ", " + firstname
        else:
            return lastname + ", " + firstname

    # Validate if input is outside the choices
    else:
        return "Invalid Sort order"


# Input Name and select what sort
x = sortName(input("Enter First Name: "), input("Last Name: "),
             input("Select Order:Enter number(1 or 2) or word(firstlast or lastfirst)\n 1.)firstlast\n 2.)lastfirst\n"))

print(x)
