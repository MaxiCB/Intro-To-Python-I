#  Write a function 'print_tuple' that prints all values in a tuple

def print_tuple(tuple):
    for item in tuple:
        print(item)

t = (1, 2, 5, 7, 99)
print_tuple(t)

# Tuples with one element need a comma after the first element in order to have the correct syntax
# This forces it to be seen as a tuple rather than a int or string
u = (1,)
print_tuple(u)