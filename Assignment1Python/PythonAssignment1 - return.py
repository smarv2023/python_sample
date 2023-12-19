# function to Validate the age
def age_validator():
    if age > 1 and age <= 5:
        return "You are very young"
    elif age > 5 and age <= 15:
        return "You are young"
    elif age > 15 and age <= 30:
        return "You are young adult"
    elif age > 30 and age <= 50:
        return "You are adult"
    elif age > 50 and age <= 65:
        return "You are middle aged"
    elif age >= 65:
        return "You are a senior citizen"
    else:
        # if they put negative number
        return "Your age is Invalid"


# Enter the name and store it
name = str(input("Enter Name: "))
print("Welcome, ", name)

# Enter the age and store it

while True:
    try:
        age = int(input("Please enter you age: "))
    except ValueError:
        print("Sorry", name, "That is not a age")
        continue
    else:
        break
print(name, age, age_validator())

