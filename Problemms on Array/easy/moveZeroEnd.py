def moveZeroToEnd(arr):
    temp_array =[]
    j =0
    for i in range(len(arr)):
        if arr[i] != 0:
            temp_array.append(arr[j])
        j +=1
    for i in range(len(temp_array), len(arr)):
        temp_array.append(0)
    arr = temp_array
    print(arr)

def optimized(arr):
    j = -1
    for i in range(len(arr)):
        if arr[i] == 0:
            j = i
            break
    if j == -1:
        return arr
    if i in range(j+1, len(arr)):
        if arr[i] != 0:
            (arr[i] , arr[j]) = (arr[j] , arr[i])
            j +=1
    print(arr)
    return arr
    

if __name__ == '__main__':
    array = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]
    arra = optimized(array)
    print(arra)
    