# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count = 0
num = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    fvalue = float(line[line.find('0'):])
    count = count + 1
    num = num + fvalue 
    
print('Average spam confidence:', num/count)
