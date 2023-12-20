class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transposed = [[] for i in range(len(matrix[0]))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                transposed[col].append(matrix[row][col])

        return transposed