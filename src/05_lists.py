x = [1, 2, 3]
y = [8, 9, 10]

# Change x so that it is [1, 2, 3, 4]

def changeX():
    x.append(4)
    print(x)

changeX()

# Using y change x so that is is [1, 2, 3, 4, 8, 9, 10]

def addYToX():
    for num in y:
        x.append(num)
    print(x)

addYToX()

# Change x so that it is [1, 2, 3, 4, 9, 10]

def remove8():
    x.pop(x.index(8))
    print(x)

remove8()

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]

def add99():
    count = len(x)
    x.insert(count - 1, 99)
    print(x)

add99()

# Print the length of list x

def xLen():
    print(len(x))

xLen()

# Print all values in x multiplied by 1000

def multX():
    for item in x:
        print(item * 1000)

multX()