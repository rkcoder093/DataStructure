'''Example 1:
Input Format
: N = 5, array[] = {1,2,2,3,2}
Result
: 2
Explanation:
 Here we can see that the Count(1) = 1, Count(2) = 3 and Count(3) = 1.Therefore, the count of 2 is greater than N/3 times. Hence, 2 is the answer.

Example 2:
Input Format
:  N = 6, array[] = {11,33,33,11,33,11}
Result:
 11 33
Explanation:
 Here we can see that the Count(11) = 3 and Count(33) = 3. Therefore, the count of both 11 and 33 is greater than N/3 times. Hence, 11 and 33 is the answer.
'''

def Solution(arr:[int]) -> [int]: # type: ignore
    count ={}
    
    for i in range(len(arr)):
        if arr[i] in count:
            count[arr[i]] += 1
        else:
            count[arr[i]] = 1

    N = len(arr)
    check_for = N/3
    solution =[]
    for i in count:
        if count[i] >check_for:
            solution.append(i)
    return solution
    
    
    
    
def main():
    array =  [2, 2, 1, 3, 1, 1, 3, 1, 1]   
    solution = Solution(array)
    for i in solution:
        print(i, end=" ")


if __name__ == '__main__':
    main()