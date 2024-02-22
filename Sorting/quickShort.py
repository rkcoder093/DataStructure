def FindPivot(arr , low, high):
    pivot = arr[low]
    i = low
    j = high 
    while(i < j):
        while arr[i] <= pivot and i<=high-1:
            i +=1
        while arr[j] > pivot and j>=low+1:
            j -= 1
        if (i<j ):
            (arr[i], arr[j]) = (arr[j] , arr[i])
    (arr[low], arr[j]) =(arr[j], arr[low])
    return j 
def quickSort(arr, low, high):
    if (low < high):
        pivot = FindPivot(arr, low , high)
        quickSort(arr,low, pivot-1,)
        quickSort(arr, pivot+1,high)
    
def printQuickSort(arr, low, high):
    quickSort(arr, low, high )
    return arr
    
array = [4,6,2,5,7,9,1,3]
sorted_array = printQuickSort(array, 0 , len(array)-1)
print(sorted_array)