# time complexity O(N^2) 
def BubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if int(arr[j]) > int(arr[j+1]):
                (arr[j], arr[j+1]) = (arr[j+1], arr[j])
    return arr

input = open('Sorting/input.txt','r')
content = input.read().split(' ')

sorted_list = BubbleSort(content)
print(sorted_list)
output = open('Sorting/output.txt' ,'w')
output.write(' '.join(sorted_list))

