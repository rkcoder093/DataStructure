# bruteoforce approach O(1)

def bruteForce(arr):
    arr = sorted(arr)
    print(arr[-2], arr[1])
    
# O(N)
def Better(arr):
    if len(arr) == 1:
        print(arr[-1], arr[0])
    second_small = float('inf')
    second_large = float('-inf')
    small = min(arr)
    large = max(arr)
    for i in range(len(arr)):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    print(second_large, second_small)

# optimized approach O(N)
def second_largest_element (arr):
    largest = float('-inf')
    second_largest = float('-inf')
    for i in range(len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] != largest:
            second_largest = arr[i]
    print(second_largest)

def second_small_element (arr):
    small = float('inf')
    second_small = float('inf')
    for i in range(len(arr)):
        if arr[i] < small:
            second_small = small
            small = arr[i]
        elif arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
    print(second_small)
    

array = [1,54,777,4,3,37,74,34]
second_largest_element(array)
second_small_element(array)