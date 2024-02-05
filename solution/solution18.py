def reverseArray(arr):
    rev = []
    for i in range(0,len(arr)):
        rev.append(arr[-1-i])
        # print(arr[-1-i])
    print(rev)
arr =[1,2,3,4,5,6]
reverseArray(arr)


def reverseArrayByRecursion(arr2,endIndex,startIndex):
    if startIndex < endIndex:
        (arr2[startIndex] , arr2[endIndex]) = (arr2[endIndex],arr2[startIndex])
        reverseArrayByRecursion(arr2 , startIndex +1, endIndex-1)
    print(arr)
    
reverseArrayByRecursion(arr,0,len(arr)-1)