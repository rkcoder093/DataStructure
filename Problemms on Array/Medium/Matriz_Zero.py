from typing import List


class Solution:
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_to_zeros = []
        column_to_zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row_to_zeros.append(i)
                    column_to_zeros.append(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in row_to_zeros or j in column_to_zeros:
                    matrix[i][j]  = 0
        print(matrix)             
                 
matrix=[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s = Solution()
s.setZeroes(matrix)