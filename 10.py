# Array Partiton I

# Print Biggest number which made by pair of min(a,b)

### Solution1 ###
def biggest_number(input: list[int])-> int:
    input.sort()
    length = len(input)
    result = 0

    for index in range(0,length,2):
        # pair
        if index+1<=length-1:
            result += min(input[index], input[index+1])
        # alone
        else:
            result += input[index]

    return result


### Solution2 ### (Just use even index, Derive method from Sol1)
def biggest_number2(input: list[int])-> int:
    input.sort()
    lenght = len(input)
    result = 0

    for index in range(0,lenght,2):
        result += input[index]

    return result

### Solution3 ### (Pythonic Method, Derive from Sol2)
def biggest_number3(input: list[int])-> int:
    return sum(sorted(input)[::2])
