"""
list comprehension practice
"""

name = 'Rudolf'
# new_list = [new_item for item in list ]
letters = [letter for letter in name.lower() ]
print(letters)
# remember list, range, tuple, string are sequences. They have a specific order

double_nums = [ n *2 for n in range(1,5)]
print(double_nums)

# conditionals work too: new_list = [ new_item for item in list if test]
names = ['Caroline', 'Dave', 'Eddie', 'Frank', 'Greg', 'Harriet', 'Isaac']
caps_names = [ name.upper() for name in names if len(name) >= 5]
print(caps_names)

fib_seq = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
fib_squares = [ n * n for n in fib_seq]
print(fib_squares)

# convert to ints and select only the even numbers
string_nums = ['1', '2', '3', '4', '5', '6', '7']
evens = [int(n) for n in string_nums if int(n) % 2 == 0]
print(evens)

