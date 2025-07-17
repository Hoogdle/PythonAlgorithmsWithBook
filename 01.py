# Valid Palindrome
import collections
import re


# "Check is given string palindrome"

# Cond #
# 1. process only alphabet and numbers
# 2. do not separate Capital and Small letters

### Solution1 ###

def is_palindrome() -> bool:
    inputs = input()

    filtered_list = []
    # get only alphabet and numbers
    for char in inputs:
        if char.isalnum():
            filtered_list.append(char.lower())

    iter_num = len(filtered_list)//2
    last_index = len(filtered_list) - 1

    for i in range(iter_num):
        if filtered_list[i] != filtered_list[last_index-i]:
            return False

    return True


### Solution2 ### (Using deque for optimizing)
def is_palindrome2() -> bool:

    user_input = input()

    filtered_str = collections.deque()

    # put only lower alphabet or numbers
    for char in user_input:
        if char.isalnum():
            filtered_str.append(char.lower())

    while len(filtered_str) > 1:
        if filtered_str.popleft() != filtered_str.pop():
            return False

    return True


### Solution3 ### (Regular Expression)
def is_palindrome3() -> bool:
    inputs = input()

    # make lower letter
    inputs = inputs.lower()

    filtered_str = re.sub('[^a-z0-9]','',inputs)
    return filtered_str[:] == filtered_str[::-1]

print(is_palindrome3())





