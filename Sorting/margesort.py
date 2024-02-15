def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1

    # Copy the elements from temp back to arr
    for i in range(len(temp)):
        arr[low + i] = temp[i]

    # print(arr)

def mS(arr, low, high):
    if low == high:
        return

    mid = (low + high) // 2
    mS(arr, low, mid)
    mS(arr, mid + 1, high)
    merge(arr, low, mid, high)

lists = [3, 1, 100, 43, 2, 345, 12, 0, 4]
length = len(lists) - 1
mS(lists, 0, length)
print(lists)
