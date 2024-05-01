def countOnes(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            count +=1
    print(count)


def countHash(arr):
    hash =[0] *2
    for i in range(len(arr)):
        hash[arr[i]] +=1
    print(hash[1])

def countinDict(arr):
    myDict = {}
    for i in range(len(arr)):
        if arr[i] in myDict:
            myDict[arr[i]] +=1
        else:
            myDict[arr[i]] = 1
    print(myDict[1])

def consecutiveOnes(arr):
    count =0
    max_count =0
    for i in range(len(arr)):
        # max_count = count
        if arr[i] == 1:
            count +=1
        else:
            count = 0
        max_count = max(count, max_count)
    print(max_count)
    
    
if __name__ == '__main__':
    array = [1,0,0,1,1,1,1,1,0,1]
    consecutiveOnes(array)