#  Write a function 'print_tuple' that prints all values in a tuple

import math

def dist(a, b):
    # This destructures the parts of the tuples provided
    x0, y0 = a 
    x1, y1 = b

    return math.sqrt((x1-x0)**2 + (y1-y0)**2)

a = (2,7)
b = (-14, 72)

print("Distance is: {:.2f}".format(dist(a, b)))

def print_tuple(tuple):
    for item in tuple:
        print(item)

t = (1, 2, 5, 7, 99)
print_tuple(t)

# Tuples with one element need a comma after the first element in order to have the correct syntax
# This forces it to be seen as a tuple rather than a int or string
u = (1,)
print_tuple(u)