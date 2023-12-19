

def print_something(name = 'Marvin', age = 'unknown'):
    print('My name is', name, 'and my age is', age)


print_something('Lizl', 35)
print_something('Lizl')
# Put variable if you want to pass to function
print_something(age=90)
# Default value
print_something()