# Function to put number 1 and number 2
def getNumbers():
    num1 = int(input('Enter number 1st number: '))
    num2 = int(input('Enter number 2nd number: '))

    # This will validate the number if above 0 and less than 0
    if num1 > 0 and num2 > 0:
        print('2 positive numbers')
    elif num1 < 0 and num2 < 0:
        print('2 negative numbers')
    elif num1 > 0 > num2:
        print(f'num1: {num1} is positive, and num2: {num2} is negative')
    elif num1 < 0 < num2:
        print(f'num1: {num1} is negative, and num2: {num2} is positive')

    # This will also validate if 1 of the numbers is positive and negative
    if num1 > 0 or num2 > 0:
        print('One number is positive')
    elif num1 < 0 or num2 < 0:
        print('One number is negative')

    # This will print the result of the two number based on:
    # Addition, Subtraction, Multiplication, and Division
    print('Addition Result: ', num1 + num2)
    print('Subtraction Result: ', num1 - num2)
    print('Multiplication Result: ', num1 * num2)

    # This will prevent the ERROR of divided by 0
    if num2 != 0:
        print('Division Result: ', num1 / num2)
    else:
        print('Undefined: Can not divided by 0')


# This is to Invoke the function
getNumbers()
