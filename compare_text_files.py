"""
import the text files
compare the numbers
output the numbers that are the same
use list compression to do so
"""

with open('file1.txt', 'r') as f:
    list1 = [int(num.strip('\n')) for num in f.readlines()]

with open('file2.txt', 'r') as f:
    list2 = [int(num.strip('\n')) for num in f.readlines()]

common_nums = [num for num in list2 if num in list1]
print(common_nums)

