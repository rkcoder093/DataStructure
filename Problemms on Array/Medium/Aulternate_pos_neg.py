
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []

        for i in range(len(nums)):
            if nums[i] > 0:
                positive.append(nums[i])
            if nums[i] < 0:
                negative.append(nums[i])
        pos = 0
        neg = 0
        for i in range(len(nums)):

            if i % 2 == 0:
                print(pos)
                nums[i] = positive[pos]
                pos = pos +1
            else:
                print(neg)
                nums[i] = negative[neg]
                neg = neg + 1
        return nums
    
    def optimanApproach(self, nums:List[int]) -> int :
        optional = [] * len(nums)
        pos = 0 
        neg = 1
        for i in range(len(nums)):
            if nums[i] > 0 :
                optional.insert(pos,nums[i])
                pos +=2
            if nums[i] < 0:
                optional.insert(neg, nums[i])
                neg +=2
        return optional
                
    
s = Solution()
array = [3,1,-2,-5,2,-4]
arr = s.optimanApproach(array)
print(arr)