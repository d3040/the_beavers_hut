# Excersice 5.1
# use words.txt as the file name

while True:
	fname = input('Enter the file name: ')
	try:
		fh = open(fname, 'r')
	except:
		print('File name not found.')
	break

for line in fh:
	n_line = line.rstrip()
	print(n_line.upper())


