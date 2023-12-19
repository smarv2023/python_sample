# function to Validate the age
def age_validator():
    if age > 1 and age <= 5:
        print(name, age, "You are very young")
    elif age > 5 and age <= 15:
        print(name, age, "You are young")
    elif age > 15 and age <= 30:
        print(name, age, "You are young adult")
    elif age > 30 and age <= 50:
        print(name, age, "You are adult")
    elif age > 50 and age <= 65:
        print(name, age, "You are middle aged")
    elif age >= 65:
        print(name, age, "You are a senior citizen")
    else:
        # if they put negative number
        print(name, age, "Your age is Invalid")


# Enter the name and store it
name = str(input("Enter Name: "))
print("Welcome, ", name)

# Enter the age and store it
age = int(input("Please enter you age: "))
age_validator()