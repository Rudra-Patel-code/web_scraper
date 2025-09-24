"""List comprehension = a comcise way to create lists in python. compact and easier to read than traditional loops
[expression for singular value in iterable if condition]
"""

# traditional loop

doubles = []  # empty list or array

for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)


doubles = [x * 2 for x in range(1, 11)]

print(doubles)
