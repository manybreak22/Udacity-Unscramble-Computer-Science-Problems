"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

arraywithNumbers = []
for each in texts:
    if each[0] not in arraywithNumbers:
        arraywithNumbers.append(each[0])
    if each[1] not in arraywithNumbers:
        arraywithNumbers.append(each[1])


for talked in calls:
    if talked[0] not in arraywithNumbers:
        arraywithNumbers.append(talked[0])
    if talked[1] not in arraywithNumbers:
        arraywithNumbers.append(talked[1])


print("There are {} different telephone numbers in the records.".format((len(arraywithNumbers))))

