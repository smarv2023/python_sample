def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


choice = input('Select operation.\n1.Add\n2.Subtract\n3.Multiply\n4.Divided\n')

num1 = int(input('Enter first number: '))
num2 = int(input('Enter first number: '))

if choice == '1':
    print(num1, '+', num2, '=', addition(num1, num2))
elif choice == '2':
    print(num1, '-', num2, '=', subtraction(num1, num2))
elif choice == '3':
    print(num1, '*', num2, '=', multiplication(num1, num2))
elif choice == '4':
    print(num1, '/', num2, '=', division(num1, num2))
else:
    print('Invalid Input')
