# Longest Palindrome Substring

# "Print longest palindrome substring"

### Solution1 ### (Using Two-Pointer)
def longest_palindrome(input: str)-> str:

    length = len(input)

    def check_palindrome(left: int, right: int)-> str:
        while left>=0 and right<length and input[left] == input[right]:
            left -= 1
            right += 1
        
        return input[left+1:right]
    
    if length<2 or input == input[::-1]:
        return input
    
    result = ''
    
    for i in range(length):
        result = max(result, check_palindrome(i,i+1), check_palindrome(i, i+2), key=len)
    
    return result
    

        