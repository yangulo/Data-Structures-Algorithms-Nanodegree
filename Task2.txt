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

# returns max duration among all numbers
def max_duration(all_records):
    max_record = 0
    result = []
    for r in all_records:
        # for iterates on dictionary keys
        if all_records[r] > max_record:
            max_record = all_records[r]
            result = [r, max_record]
    return result 

# Returns the sum of the duration of each unique number in calls
def max_time_on_phone(calls):
    new_calls = dict()
    for c in calls:
        if c[0] not in new_calls: 
            new_calls[c[0]] = int(c[3])
        else:
            new_calls[c[0]] += int(c[3])
        if c[1] not in new_calls:
            new_calls[c[1]] = int(c[3])
        else:
            new_calls[c[1]] += int(c[3])        
    return '{} spent the longest time, {} seconds, on the phone during September 2016.'.format(max_duration(new_calls)[0], 
                                                                                               max_duration(new_calls)[1] )
            
print(max_time_on_phone(calls))    
