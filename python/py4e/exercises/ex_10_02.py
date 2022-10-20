# 10.2 Write a program to read through the mbox-short.txt and 
# figure out the distribution by hour of the day for each of 
# the messages. You can pull the hour out from the 'From ' line
# by finding the time and then splitting the string a second
# time using a colon.
#
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#
# Once you have accumulated the counts for each hour, print out
# the counts, sorted by hour as shown below.


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hour_histogram = dict()

for line in handle:
    words = line.split()
    if len(words) > 2 and words[0] == "From":
        time = words[5].split(":")
        h = time[0]
        hour_histogram[h] = hour_histogram.get(h, 0) + 1

histogram_list = list()

for k, v in hour_histogram.items():
    histogram_list.append((k, v))
    
histogram_list.sort()

[print(k, v) for k, v in histogram_list]