from art import logo


# Calculator

# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def sub(n1, n2):
    return n1 - n2


# Multiply
def mul(n1, n2):
    return n1 * n2


# Divide
def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def calculator():
    print(logo)
    run = True
    num1 = float(input("Enter first number: "))
    while run:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Choose an operation: ")
        num2 = float(input("Enter next number: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        choice = input(
            f"Type 'y' to continue calculating with {answer}, 'n' to start new: \n type 'quit' to exit\n").lower()
        if choice == "y":
            num1 = answer
        elif choice == "quit":
            break
        else:
            calculator()


calculator()
