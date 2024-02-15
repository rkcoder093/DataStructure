# time complexity O(N^2) 
def SelcetionSort(arr):
    for i in range(len(arr)-1):
        min = i
        for j in range(i, len(arr)):
            if int(arr[j]) < int(arr[min]):
                min = j
 
        (arr[min], arr[i]) = (arr[i], arr[min])
    return arr
        

input = open('sorting/input.txt', 'r')
content = input.read().split(" ")

sorted_array = SelcetionSort(content)

output = open('sorting/output.txt', 'w')
write  = output.write(' '.join(sorted_array)) 

