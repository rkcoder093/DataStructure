# time complexity O(N^2) 
def insersionSort(arr, index , n):
    if index == n :
        return     
    j = index
    while (j > 0 and int(arr[j-1]) > int(arr[j])):
        (arr[j-1] , arr[j]) = (arr[j], arr[j-1])
        j -=1
    insersionSort(arr, index+1 , n)
    return arr


input = open('sorting/input.txt','r')
array = input.read().split()
print(array)
sorted_array = insersionSort(array, 0 , len(array))

output = open('sorting/output.txt','w')
output.write(" ".join(sorted_array))