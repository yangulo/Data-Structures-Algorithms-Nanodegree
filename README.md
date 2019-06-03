# Worst Case Big O Notation Analysis

# Task 0
The complexity of this algorithm is O(1). We know that the index of the result will always be the same and it won't change with any increase in "n".

# Task 1
The complexity of this algorithm is O(n). We can assume that the texts' universe will be "n" and the calls' universe "m". However, we know that the n+m will be the entire universe therefore n = n + m. Since we have two "for" in the code,  we are iterating twice. Therfore the complexity will be O(2n) but in Big O we drop the constans so the final solution will be O(n). 

# Task 2
The complexity of this algorithm is O(n). "max_time_on_phone" function has only one for therefore the complexity will be O(n), "max_time_on_phone" function is calling "max_duration" function but "max_duration" iterates with a subset of n, that means that max_duration's n is smaller. We can assume that "max_duration" is O(n/2), therefore the complexity will be O(1.5n) but as mentioned before, in Big O notation we drop the constants so the final solution is O(n)

# Task 3
The complexity of "area_codes" algorithm is O(n log n) and the complexity of "porcentage_calls" is O(n). As per "area_codes" there is only one "for" therfore the complexity will be O(n) but since it returns a sorted list, the complexity of sorted() is O(n log n). The entire complexity will be O(n log n) + O(n) but "n" is a constant and it can be droped so "area_codes" complexity is O(n log n).

# Task 4
The complexity of "telemarketers" is O(n log n). "telemarketers" has only one "for" which will be O(n) complexity, however it calls "only_callers" and "callers_not_in_texts" of O(n) each, also "telemarketers" returns a sorted list of O(n log n). So the entire complexity will be O(n log n) + O(3n). Nevertheless as mentioned before constants can be droped, and so the final result is O(n log n) for telemarketers function.