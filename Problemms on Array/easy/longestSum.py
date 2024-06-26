from typing import List


class Solution:
    def getLongestSubarray(self, a: List[int], k: int) -> int:
        n = len(a) # size of the array.
        length = 0
        for i in range(n): # starting index
            for j in range(i, n): # ending index
                # add all the elements of
                # subarray = a[i...j]:
                s = 0
                for K in range(i, j+1):
                    s += a[K]
                if s == k:
                    length = max(length, j - i + 1)
        return length
    
    
if __name__ =='__main__':
    array = [1,2,3,4,5,1,9]
    obj = Solution()
    lists =obj.getLongestSubarray(array, 5)
    print(lists)