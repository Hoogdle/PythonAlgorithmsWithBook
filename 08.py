# Trapping Rain Water

### Caculate quantity of stacked water with given height.

### Solution1 ### (Two-Pointer)
def cal_water(wall: list[int])-> int:
    length = len(wall)
    left_index, right_index = 0, length-1
    water = 0

    left_max, right_max = wall[left_index], wall[right_index]

    while left_index < right_index:
        if left_max < right_max:
            left_max = max(left_max, wall[left_index])
            water += left_max - wall[left_index]
            left_index += 1
        else:
            right_max = max(right_max, wall[right_max])
            water = right_max - wall[right_max]
            right_max -= 1
    
    return water
