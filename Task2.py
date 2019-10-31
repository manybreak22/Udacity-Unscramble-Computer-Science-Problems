"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

longest_time = {}

for record in calls:
    phone1 = record[0]
    phone2 = record[1]

    if phone1 not in longest_time :
        longest_time [phone1] = int(record[3])
    else:
        longest_time [phone1] += int(record[3])

    if phone2 not in longest_time :
        longest_time [phone2] = int(record[3])
    else:
        longest_time [phone2] += int(record[3])


key = max(longest_time , key=lambda k: longest_time [k])
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(key, longest_time [key]))

