# optimized approach
def largestinArrar(arr):
    element = arr[0]
    for i in range(1,len(arr)):
        if element < arr[i]:
            element = arr[i]
    return element

# .bruteforce approach
def largesrnumber(arr):
    arr = sorted(arr)
    print(arr[-1])  
    
    
array = [999,2,3,100,6,7,8]
largesrnumber(array)
