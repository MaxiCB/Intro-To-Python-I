# Write a function is_even that will return true if it the passed number is even

def is_even(num):
    if num % 2 == 0:
        return ['Even!', True]
    else:
        return ['Odd!', False]

num = input('Enter a number')
num = int(num)

print(is_even(num))