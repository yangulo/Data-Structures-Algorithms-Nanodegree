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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Returns only numbers called
def only_callers(callers, receivers):  
    tmp = set(callers)
    for call in callers:
        if call in receivers:
            tmp.remove(call)
    return tmp

# Returns numbers called but that never sent nor received a text
def callers_not_in_texts(callers, texts):
    for call in texts:
        if call[0] in callers:
            callers.remove(call[0])
        if call[1] in callers:
            callers.remove(call[1])
    return callers

# Returns possible telemarketers numbers, which never received a call, nor sent/received a text
def telemarketers(calls, texts):
    callers = set()
    receivers = set()
    for call in calls:
        callers.add(call[0])
        receivers.add(call[1])
    c = only_callers(callers, receivers)
    result = callers_not_in_texts(c, texts)
    
    return 'These numbers could be telemarketers: \n{}'.format('\n'.join(sorted(result)))

print(telemarketers(calls, texts))

