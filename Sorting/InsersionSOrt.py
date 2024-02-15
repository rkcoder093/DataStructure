# time complexity O(N^2) 
def insersionSort(arr):
    for i in range(0,len(arr)):
        j = i
        print(i)
        while ((j > 0) and (arr[j-1] > arr[j])):
            (arr[j], arr[j-1])=(arr[j-1] , arr[j])
            j -=1
            print(j,f'{arr[j]} {arr[j-1]}', sep=":")
        print()
    return arr

input = open('sorting/input.txt','r')
array = input.read().split()

sorted_array = insersionSort(array)

output = open('sorting/output.txt','w')
output.write(" ".join(sorted_array))