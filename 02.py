#Reverse String

# Make a function that reverse string.
# Input is Array of Char
# Do not make any return, control given input as itself

### Solution1 ### (Using Slicing)
def reverse_string(input: list[str])-> None:
    # use '[:]' for deep copy
    input[:] = input[::-1]

### Solution2 ### (Using Two-Pointer)
def reverse_string2(input: list[str])-> None:
    left, right = 0, len(input)-1

    while left<right:
        input[left], input[right] = input[right], input[left]
        left += 1
        right -= 1
