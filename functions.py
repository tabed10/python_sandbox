# A function is a block of code which only runs when it is called.
# In Python, we do not use parentheses and curly brackets, we use indentation with tabs or spaces


# Create function
def say_hello(name='Sam'):
    """
    Prints Hello and then name.
    """
    print('Hello ' + name)


# Return value
def get_sum(num1, num2):
    total = num1 + num2
    return total


numSum = get_sum(2, 3)


def add_one_to_num(number):
    number += 1
    return number


num = 5
new_num = add_one_to_num(num)
print(new_num)


# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Very similar to JS arrow functions


get_sum = lambda num1, num2: num1 + num2
print(get_sum(9, 2))


add_one_to_num = lambda num1: num1 + 1
print(add_one_to_num(5))
