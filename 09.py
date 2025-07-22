# 3Sum

### Print 3 elements, summation of these are zero

### Solution1 ### (Brute-Force)

import time
def three2zero(nums: list[int])-> list[list[int]]:
    nums.sort()
    length = len(nums)
    
    result = []

    for first in range(length-2):
       for second in range(first+1, length-1):
            if nums[first] + nums[second] > 0:
                break
            for third in range(second+1,length):
                if nums[first] + nums[second] + nums[third] > 0:
                    break
                elif nums[first] + nums[second] + nums[third] == 0:
                    result.append([nums[first], nums[second], nums[third]])

    return result


### Solution2 ### (Two-Pointer)
def three2zero2(nums: list[int])-> list[list[int]]:
    nums.sort()
    length = len(nums)

    result = []

    for pivot in range(length-2):
        left, right = pivot+1, length-1
        target = nums[pivot]

        while left<right:
            summation = target + nums[left] + nums[right]
            if summation > 0:
                right -= 1
            elif summation < 0 :
                left += 1
            elif summation == 0:
                result.append([target,nums[left],nums[right]])
                left += 1

    return result


