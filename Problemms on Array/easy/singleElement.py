from typing import List


class Solution:
    def SingleElement(self, nums:List[int]) -> int :
        count ={}
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] =1
        num =0
        for i in count:
            if count[i] == 1:
                num = i   
        return num
    
    def BruteForce(self, arr: List[int]) -> int:
        count =0
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] == arr[j]:
                    count +=1
            if count == 1:
                return arr[i]
            else:
                count = 0
                
    def xorAproach(self, arr: List[int]) ->  int :
        xor = 0
        for i in arr:
            xor ^= i
        return xor

if __name__ =='__main__':
    array = [1,2,3,4,5,67,1,2,3,4,5]
    obj = Solution()
    single_element = obj.xorAproach(array)
    print(single_element)