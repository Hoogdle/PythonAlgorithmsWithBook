# Product of Array Except Self

# Return the array, elements are result of multiplication except itself.
# Make a Alogirithm with O(n) Complexity.

### Solution1 ###

import collections
import numpy as np

def mul_without_itself(nums: list[int])-> list[int]:
    from_left = [1]
    from_right = collections.deque([1])    
    length = len(nums)

    for i in range(length-1):
        left_value = nums[i] * from_left[len(from_left)-1]
        from_left.append(left_value)

    for i in range(length-1):
        reversed_i = length - (i+1)
        right_value = nums[reversed_i] * from_right[0]
        from_right.appendleft(right_value)
    
    np_from_left = np.array(from_left)
    np_from_right = np.array(from_right)
    return (np_from_left * np_from_right).tolist()

user_input = [1,2,3,4]
print(mul_without_itself(user_input))