def LeftRotate (arr):
    element = arr.pop(0)
    arr.append(element)
    print(arr)
    
def bruteForce(arr):
    temp =[]
    for i in range(1, len(arr)):
       temp.append(arr[i])
    temp.append(arr[0])
    print(temp)
    
def optimizedApproach(arr):
    temp = arr[0]
    for i in range(0, len(arr)-1):
        arr[i] = arr[i+1]
    arr[-1] = temp
    print(arr)
    
def mySwap(arr):
    for i in range(len(arr)-1):
        (arr[i], arr[i+1]) = (arr[i+1], arr[i])
    print(arr)
    
    
if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9]
    mySwap(array)