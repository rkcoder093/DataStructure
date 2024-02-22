def LinearSearch(arr, n):
    for i in range(len(arr)):
        if arr[i] == n :
            return i
            break
        return -1


if __name__ == '__main__':
    array = [1,2,3,4,56,7,8,9,10]
    num = 2
    find = LinearSearch(array, num)
    if find != -1:
        print (f'your number {num} is present at the index {find}')
    elif find == -1:
        print(f'you are number {num} is not in the list {array}') 