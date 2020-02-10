# Print out 2 to the 65536'th power

# To calculate the power of a number it is
# num * num for every iteration of the power supplied
# i.e 7 * 7 * 7 * 7 is 7 to the power of 4

def bigNum(num, power):
    result = num ** power
    print(result)
    
bigNum(2, 65536)