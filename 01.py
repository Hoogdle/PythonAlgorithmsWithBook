# Valid Palindrome

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


### Solution2 ###


