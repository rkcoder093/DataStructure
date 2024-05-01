# brute force appreach

def Solution1(array)-> int: 
    maxi  = 0
    for i in range(len(array)):
        for j in range(i, len(array)):
            sum = 0 
            for k in range(i, j+1):
                
                sum += array[k]
            
            maxi = max(sum , maxi)
    return maxi
def leetcode(nums):
    max_sub_array = nums[0]
    current_sub_array = nums[0]
    for num in nums[1:]:
        print(current_sub_array, max_sub_array)
        current_sub_array = max(current_sub_array, 0) + num
        max_sub_array = max(current_sub_array, max_sub_array)
    return max_sub_array
arr = [-2,1,-3,4,-1,2,1,-5,4]
largest_numebr = leetcode(arr)
print(largest_numebr)