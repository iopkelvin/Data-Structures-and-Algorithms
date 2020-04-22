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

numbers_dict = dict()

for call in calls:
    # Caller entry into dictionary
    if call[0] not in numbers_dict:
        numbers_dict[call[0]] = int(call[3])
    else:
        numbers_dict[call[0]] += int(call[3])
    # Receiver entry into dictionary
    if call[1] not in numbers_dict:
        numbers_dict[call[1]] = int(call[3])
    else:
        numbers_dict[call[1]] += int(call[3])

longest_time = max(numbers_dict, key=numbers_dict.get)
print('{} spent the longest time, {} seconds on the during September 2016.'.format(longest_time, numbers_dict[longest_time]))

