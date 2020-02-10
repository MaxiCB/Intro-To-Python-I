# Practicing using printf, format string method, and using f-strings

# Using the printf operator (%), print the following feeding the values of x, y, and z:
#  x is 10, y is 2.25, z is "I Like Turtles"

def printfOperator():
    print("x is %2d, y is %2.2f, z is %2s" % (10, 2.25, "I Like Turtles!"))

printfOperator()
# Use the 'format string to do the same

def formatString(x, y, z):
    print("x is {x}, y is {y}, z is {z}".format(x=x, y=y, z=z))

formatString(10, 2.25, "I Like Turtles!")
# # Use f-string to do the same

def fString(x, y, z):
    print(f"x is {x}, y is {y}, z is {z}")

fString(10, 2.25, "I Like Turtles!")