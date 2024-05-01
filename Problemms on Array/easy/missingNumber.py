def missingNumber(arr): 
    missing_number =[]
    for i in range(arr[0], arr[-1]):
        if i not in arr:
            missing_number.append(i)
    print(arr, missing_number)
    return missing_number

def betterA(arr):
    hash = [0] *(arr[-1] +1)
    missing=[]
    for i in range(len(arr)):
        hash[arr[i]] += 1
        
    for i in range(1, len(hash)):
        if hash[i] == 0:
            missing.append(i)
    print(arr, hash )
    return missing


if __name__ == '__main__':
    array = [1,2,4,5,7,8,11]
    missing = betterA(array)
    for i in missing:
        print(i)