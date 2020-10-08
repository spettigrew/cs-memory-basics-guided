"""
Given a list of integers `lst`, any integer with a frequency that is equal to its value is considered a **lucky integer**.

Write a function that returns the lucky integer from the array. If the array contains multiple lucky integers, return the largest one. If there are no lucky integers return -1.

**Example 1**:

Input: arr = [2,3,3,3,4]
Output: 3

**Example 2**:

Input: arr = [1,2,2,3,3,3,4,4,4,4]
Output: 4

**Example 3**:

Input: arr = [1,1,2,2,2]
Output: -1
"""
def find_lucky(lst):
    # UNDERSTAND
    # if the count = value, return the value
    # PLAN
    # Define an output variable
    # overall runtime:
    # constant + n log n (for the sort) + n * n --> O(n^2)
    # 1 + n log n + n^2
    # space complexity: O(n)
    output = -1             # constant
    # Sort the list from largest to smallest
    lst.sort(reverse=True)  # sort --> O(n log n), in place
    # Make a set
    set_list = set(lst)     # O(n)
    # Iterate through the set, counting the # of times each value shows up
    for number in set_list:             # how many times does the loop run? potentially n times.
        # Make a count variable
        count = lst.count(number)       # O(n): the number of operations grows with the size of lst
        # Check if the count == the value
        if number == count:             # O(1)
            # If it does, add it to output variable
            output = number             # O(1)
    # If nothing matches, return -1
    return output
# def count(lst, number):
#     count = 0
#     for n in lst:
#         if n == number:
#             count += 1
#     return count
#
def find_lucky_2(lst):
    # overall runtime with count outside of loop:
    # 1 + n log n  + n --> n log n
    # space complexity: O(n)
    output = -1             # constant
    # Sort the list from largest to smallest
    lst.sort(reverse=True)  # sort --> O(n log n), in place
    # count the number of times each element appears in the lst
    counts = {}
    for number in lst:      # O(n)
        if number not in counts:
            counts[number] = 0
        counts[number] += 1
    # Make a set
    set_list = set(lst)     # O(n)
    # Iterate through the set, counting the # of times each value shows up
    for number in set_list:             # how many times does the loop run? potentially n times.
        # Make a count variable
        count = counts[number]           # O(1)
        # Check if the count == the value
        if number == count:             # O(1)
            # If it does, add it to output variable
            output = number             # O(1)
    # If nothing matches, return -1
    return output