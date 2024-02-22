# O(K)

def RotateArray(arr, length, k , side):
    if side == 'left':
        for i in range(k):
            element = arr.pop(0)
            arr.append(element)
    elif side == 'right':
        for i in range(k):
            element = arr.pop(-1)
            arr = [element]+ arr
    return arr

def RotateArray(arr,side, length, k):
    if side == 'left':
        for i in range(k):
            element = arr.pop(0)
            arr.append(element)
    elif side == 'right':
        for i in range(k):
            element = arr.pop(-1)
            arr = [element]+ arr
    return arr


if __name__ == '__main__':
    array = [1,2,3,4,5,6,7]
    place = 3
    side = 'right'
    rotate = RotateArray(array, side, len(array), place)
    print(rotate)