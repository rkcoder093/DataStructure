# def remove(arr):
#     array = set(arr)
#     array = list(array)
#     return array



# a = [1,1,1,1,34,5,6,55,5,5,55,5,7,7]
# removed  = remove(a)
# print(removed)


from typing import List

def removeDuplicates(arr: List[int]) -> int:
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 3]
    k = removeDuplicates(arr)
    print("The array after removing duplicate elements is ")
    for i in range(k):
        print(arr[i], end=" ")
