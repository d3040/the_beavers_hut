'''
Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers.
You will extract all the numbers in the file and compute the sum of the numbers. 
'''
import re 

h_file = open('regex_sum_1226872.txt')

data_in_file = h_file.read()

list_of_numbers = re.findall('[0-9]+', data_in_file)

sum_of_numbers = 0

for number in list_of_numbers:
	sum_of_numbers += int(number)

print(len(list_of_numbers), sum_of_numbers)

# Just for fun!

print(sum([int(number) for number in re.findall('[0-9]+',open('regex_sum_1226872.txt').read())]))