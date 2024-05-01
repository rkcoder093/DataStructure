def Union(arr1, arr2):
    temp =[]
    for i in arr1:
        if i not in temp:
            temp.append(i)
    for i in arr2:
        if i not in temp:
            temp.append(i)
    print(temp)
        
def Union2(arr1,arr2):
    full_arr = arr1 +arr2
    full_arr = list(set(full_arr))
    print(full_arr)
    
    
if __name__ == '__main__':
    array1  =[1,2,13,4]
    array2  =[3,4,5,1,2,6]
    Union2(array1, array2)
    