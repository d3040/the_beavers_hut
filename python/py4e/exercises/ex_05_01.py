# Excersice 5.1
# Total count and average

largest_num = None
smallest_num = None

while True :
	sval = input('Enter a number: ')
	if sval == "done":
		break
	try:
		num = int(sval)
	except:
		print('Invalid input')
		continue
	#print(sval)
	# accumulator pattern 
	if largest_num is None:
		largest_num = num
		smallest_num = num	
	elif largest_num < num:
		largest_num = num
	elif smallest_num > num:
		smallest_num = num
	else:
		continue

#print('All done')
print("Maximum is", largest_num)
print("Minimum is", smallest_num)