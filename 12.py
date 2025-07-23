# Best Time to Buy and Sell Stock

### Find Maximum Stock Value

### Solution1 ### (Brute-Force) 
def best_stock(stocks: list[int])-> int:
    max = float('-inf')
    for i in range(len(stocks)-1):
        for j in range(i+1,len(stocks)):
            value = stocks[j] - stocks[i]
            if value > 0 and value > max:
                max = value
    
    return max

### Solution2 ### (Optimal) 
def best_stock2(stocks: list[int])-> int:
    max = 0
    smallest = float('inf')

    for item in stocks:
        if item < smallest:
            smallest = item
        
        value = item - smallest

        if value > max:
            max = value

    return max

user_input = [7,1,5,3,6,4]
print(best_stock(user_input)) #5
print(best_stock2(user_input)) #5
