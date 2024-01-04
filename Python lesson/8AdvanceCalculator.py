'''
    Program: Advance Calculator
    Author:
    Copyright:

'''

# Remove
import re

print('Our Magical Calculator')
print("Type 'quit' to exit\n")

previous = 0
run = True


def performMath():
    global run
    global previous
    # equation = ''
    if previous == 0:
        equation = input('Enter number operation number example(1+1): \n')
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print('Good bye')
        run = False
    else:
        equation = re.sub('[a-zA-Z]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

        # print('You typed', previous)


while run:
    performMath()
