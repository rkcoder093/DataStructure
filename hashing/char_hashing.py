def smallSearch(arr , number):
    print(arr, num)
    hash =[0] *26
    for i in range(len(arr)):
        hash[ord(arr[i]) - ord('a')] +=1
    occurace = hash[ord(number) - ord('a')]    
    print(f'occourance of your {number} is {occurace}')

def caltilixedSearch(arr , number):
    print(arr, num)
    hash =[0] *26
    for i in range(len(arr)):
        hash[ord(arr[i]) - ord('A')] +=1
    occurace = hash[ord(number) - ord('A')]    
    print(f'occourance of your {number} is {occurace}')  
    
def mixedSearch(arr , number):
    print(arr, num)
    hash =[0] *256
    for i in range(len(arr)):
        hash[ord(arr[i])] +=1
    occurace = hash[ord(number)]    
    print(f'occourance of your {number} is {occurace}')  
arr = 'RITIKkumarkeshri'
num = 'k'
mixedSearch(arr,num )