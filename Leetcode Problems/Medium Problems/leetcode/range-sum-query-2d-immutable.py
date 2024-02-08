class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefixSum = [[0]*len(matrix[0]) for i in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(j == 0):
                    self.prefixSum[i][j] += matrix[i][j]
                else:
                    self.prefixSum[i][j] = matrix[i][j] + self.prefixSum[i][j-1]

        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                    self.prefixSum[i][j] += self.prefixSum[i-1][j]
              
         
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        prefTop = self.prefixSum[row1 -1][col2] if row1> 0 else 0
        prefLeft = self.prefixSum[row2][col1- 1] if col1 > 0 else 0
        prefDiag = self.prefixSum[row1 - 1][col1 - 1] if col1 > 0 and row1 > 0 else 0

        return self.prefixSum[row2][col2] - prefTop - prefLeft + prefDiag



        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)