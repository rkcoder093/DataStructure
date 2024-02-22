def checkSorted(arr):
    sortedCheck = False
    for i in range(1,len(arr)-1):
        if arr[i-1] < arr[i] and arr[i] < arr[i+1]:
            sortedCheck = True
        else:
            sortedCheck = False
            break
    return sortedCheck

array = [1,2,31,4,5,6,7]
che = checkSorted(array)
if che == True:
    print('array is sorted')
elif che == False:
    print('array is not sorted')

