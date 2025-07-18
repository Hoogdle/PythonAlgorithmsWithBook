# Reorder Log Files

# "Reorder Given Log Files"

# Cond #
# 1. Most front item in log is identifier
# 2. char is before than numbers
# 3. if contents of char is same, identifier used for ordering 
# 4. log of numbers get ordered as order of input sequence

### Solution1 ### (Using Lambda as key of sorting)

def reorder_log(logs: list[str])-> list[str]:

    letters = []
    numbers = []

    for item in logs:
        if item.split()[1].isdigit():
            numbers.append(item)
        else:
            letters.append(item)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letters + numbers



