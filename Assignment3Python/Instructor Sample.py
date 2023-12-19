# Function Definition

def sortName(firstname, lastname, sortorder="firstlast"):
    if sortorder == "firstlast":
        # instead of printing directly from the function
        # we can return the value and use it that way
        # print(firstname + " " + lastname)
        return firstname + " " + lastname
    elif sortorder == "lastfirst":
        # print(lastname + " " + firstname)
        return lastname + " " + firstname
    else:
        # another response can be for validation.
        return "Invalid sortorder."


sortName(input("Enter"), input("Enter"), input("firstlast or lastfirst"))

print(sortName())
