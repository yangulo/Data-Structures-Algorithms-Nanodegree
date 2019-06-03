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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# Returns the first record in texts file
def firts_record_text(texts):
    return 'First record of texts, {} texts {} at time {}'.format(texts[0][0], texts[0][1], texts[0][2])

# Returns last record in calls file
def firts_record_calls(calls):
    last_number = len(calls)-1
    return 'Last record of calls, {} calls {} at time {}, lasting {} seconds.'.format(calls[last_number][0], 
                                                                                 calls[last_number][1],
                                                                                 calls[last_number][2],
                                                                                 calls[last_number][3])

print(firts_record_text(texts))
print(firts_record_calls(calls))
