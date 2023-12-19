# function to Validate the age
def age_validator():
    if 1 <= age <= 5:
        return "You are very young"
    elif 5 < age <= 15:
        return "You are young"
    elif 15 < age <= 30:
        return "You are young adult"
    elif 30 < age <= 50:
        return "You are adult"
    elif 50 < age <= 65:
        return "You are middle aged"
    elif age >= 65:
        return "You are a senior citizen"
    else:
        # if they put negative number
        return "Your age is Invalid"


# Enter the name and store it
name = input(str("Enter Name: "))
print("Welcome, ", name)

# Enter the age and store it

while True:
    try:
        age = int(input("Please enter you age: "))
    except ValueError:
        print("Sorry", age, "That is not a age")
        continue
    else:
        break
print(name, age_validator())
