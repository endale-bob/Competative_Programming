class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])

        result = []

        sign = True
        ind = [0,0]
        while(len(result) < cols*rows):
            result.append(mat[ind[0]][ind[1]])
            if(sign):
                ind = [ind[0] -1, ind[1] + 1]            
                if(ind[1] >= cols):
                    ind[0], ind[1] = ind[0] + 2, cols - 1
                    sign = False
                elif(ind[0] < 0):
                    ind[0] = 0
                    sign = False
            else:
                 ind = [ind[0]  + 1, ind[1] - 1]
                 if(ind[0] >= rows):
                    ind[0], ind[1] = rows - 1, ind[1] + 2
                    sign = True
                 elif(ind[1] < 0):
                    ind[1] = 0
                    sign = True

        return result