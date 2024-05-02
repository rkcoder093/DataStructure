'''
Example 1:
Input:
 nums = [-1,0,1,2,-1,-4]

Output:
 [[-1,-1,2],[-1,0,1]]

Explanation:
 Out of all possible unique triplets possible, [-1,-1,2] and [-1,0,1] satisfy the condition of summing up to zero with i!=j!=k

Example 2:
Input:
 nums=[-1,0,1,0]
Output:
 Output: [[-1,0,1],[-1,1,0]]
Explanation:
 Out of all possible unique triplets possible, [-1,0,1] and [-1,1,0] satisfy the condition of summing up to zero with i!=j!=k
'''
def Solution(arr:[int])->[int]:
    final_list = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            for k in range(j , len(arr)):
                lists = []
                sum = arr[i]+ arr[j]+ arr[k]
                if sum == 0 and i !=j != k:
                    print(i,j,k)
                    lists.append(arr[i])
                    lists.append(arr[j])
                    lists.append(arr[k])
                    final_list.append(lists)
    print(final_list)


def main():
    nums = [-1,0,1,0]
    solution = Solution(nums)


if __name__ == '__main__':
    main()