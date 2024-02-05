class Elemtnt:
    def __init__(self, arr):
        self.arr = arr
        print(arr)
    def min(self):
        min = self.arr[0]
        for i in range(0, len(self.arr)):
            if min > self.arr[i]:
                min = self.arr[i]
        return min
    def max(self):
        max = self.arr[0]
        for i in range(0, len(self.arr)):
            if max < self.arr[i]:
                max = self.arr[i]
        return max
        
list1 = [4,11,21,1,20,1,22,40,3,50,45,67]
obj = Elemtnt(list1)
min = obj.min()
max = obj.max()
print(min, max ,sep=" ")