class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        counter = 0
        result = []
        N = len(matrix)*len(matrix[0])

        def findNext(n):
            result.extend(matrix.pop(0))
            if(len(result) == N): return
            for ind in range(len(matrix) - 1):
                result.append(matrix[ind].pop())
            if(len(result) == N): return
            result.extend(reversed(matrix.pop()))
            if(len(result) == N): return
            for ind in range(len(matrix)-1, 0, -1):
                result.append(matrix[ind].pop(0))
            
        
        while(len(result) < N):
            findNext(counter)
            counter += 1
        
        
        return result
            