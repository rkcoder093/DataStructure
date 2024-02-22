# time complexity O(N^2) 
def insersionSort(arr):
    for i in range(0,len(arr)):
        j = i
        while (j > 0 and int(arr[j-1]) > int(arr[j])):
            (arr[j-1] , arr[j]) = (arr[j], arr[j-1])
            j = j-1
    return arr

input = open('sorting/input.txt','r')
array = input.read().split()
print(array)
sorted_array = insersionSort(array)

output = open('sorting/output.txt','w')
output.write(" ".join(sorted_array))