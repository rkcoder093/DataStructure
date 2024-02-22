# time complexity O(N^2)  
def BubbleSort(arr,n):
    if n == 1 :
        return
    for j in range(n-1):
        if int(arr[j]) > int(arr[j+1]):
            (arr[j], arr[j+1]) = (arr[j+1], arr[j])
    BubbleSort(arr , n-1)
    return arr

input = open('Sorting/input.txt','r')
content = input.read().split(' ')
print(len(content))
sorted_list = BubbleSort(content,len(content))
print(sorted_list)
output = open('Sorting/output.txt' ,'w')
output.write(' '.join(sorted_list))

