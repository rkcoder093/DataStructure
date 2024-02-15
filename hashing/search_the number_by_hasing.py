def search(arr , number):
    print(arr, num)
    hash =[0] *13
    for i in range(len(arr)):
        hash[arr[i]] +=1
        # print(hash[i])
    print(hash)
    print(f'number of occrance of your given number is {hash[number]} and the number is {number}')
        
    
    
arr = input()
num = int(input())
search(arr,num )