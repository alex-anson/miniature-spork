# LIST COMPREHENSION #
# EXAMPLE 1:
numbers = [34, 95, 84, 26, 28, 21, 11, 12]
# Filter out the even numbers.
# With for loop & if statement:
odd_nums = []
for n in numbers:
    if n % 2 != 0:
        odd_nums.append(n)
print(odd_nums)
# With list comprehension (filter odds out)
even_nums = [n for n in numbers if n % 2 == 0]
print(even_nums)

print('-- Begin example 2 --')
# EXAMPLE 2:
# Manipulate the object you're adding to the list
# Add powers of 2 to the new list
numbers = [1, 2, 3, 4, 5, 6]
powers_of_2 = [2 ** x for x in numbers]
print(powers_of_2)
powers_of_2 = [2 ** x for x in range(7)]
print(powers_of_2)
print([2 ** x for x in range(11) if x % 5 == 0])

