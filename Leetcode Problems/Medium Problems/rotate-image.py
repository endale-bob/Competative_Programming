class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # ind = 0
        # while(ind < len(matrix)/2):
        #     for j in range(len(matrix) - 1 - (2*ind)):
        #         matrix[ind][j], matrix[ind + j][-1-ind] = matrix[ind + j][-1-ind], matrix[ind][j]
        #         matrix[ind][j], matrix[-1-ind][-1-ind-j] = matrix[-1-ind][-1-ind-j], matrix[ind][j]
        #         matrix[ind][j], matrix[-1-ind-j][-1-ind] = matrix[-1-ind-j][-1-ind], matrix[ind][j]
        #     ind += 1
        
        for n in range(len(matrix)):
            for m in range(n, len(matrix)):
                matrix[n][m], matrix[m][n] = matrix[m][n], matrix[n][m]
        for row in matrix:
            row.reverse()

