# Two Sum

# "Return the indexs which are summed to produce target number"

### Solution1 ### (Brute-Force)
def two_sum(nums: list[int], target: int)-> list[int]:
    length =  len(nums)

    for index_l in range(length-1):
        for index_r in range(index_l+1,length):
            if nums[index_l] + nums[index_r] == target:
                return [index_l, index_r]

### Solution2 ### (Using 'in')
def two_sum(nums: list[int], target: int)-> list[int]:
    for index, item in enumerate(nums):
        complement = target - item

        if complement in nums[index+1:]:
            return [nums.index(item), nums[index+1:].index(complement)+(index+1)]
                

### Solution3 ### (Using Dictionary)
def two_sum(nums: list[int], target: int)-> list[int]:
    key_value = {}
    length = len(nums)

    for index, item in enumerate(nums):
        key_value[item] = index
    
    for index, item in enumerate(nums):
        complement = target - item

        if complement in key_value and index != key_value[complement]:
            return [key_value[complement], index]

### Solution4 ### (Edit Solution3)
def two_sum(nums: list[int], target: int)-> list[int]:
    nums_map = {}

    for index, item in enumerate(nums):
        if target - item in nums_map:
            return [index, nums_map[item]]
        nums_map[item] = index
    
