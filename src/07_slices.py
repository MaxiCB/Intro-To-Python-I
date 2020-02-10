a = [2, 4, 1, 7, 9, 6]

# Output the second element
print('Second Element')
print(a[1])

# Output the second to last element
print('Second to last Element')
print(a[len(a) - 2])

# Output the last three elements

print('Last Three Elements')
count = len(a)
start = count - 3
for value in range(start, count):
    print(a[value])

# Output the middle two elements

print('Middle Elements')
middle = count // 2

for value in range(middle - 1, middle + 1):
    print(a[value])

# Output every element except the first one

print('Every Element except first')
for value in range(1, count):
    print(a[value])

# Output every element except the last one

print('Every element except the last')
for value in range(0, count - 1):
    print(a[value])

#  For string s...

s = "Hello, World!"

# Output just the 8th-12th characters. "world"

print('8-12th Characters in string')
output = ''
for value in range(7, 12):
    print(s[value])