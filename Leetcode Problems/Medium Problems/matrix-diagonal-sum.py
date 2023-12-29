class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0

        ind = 0
        for m in mat:
            result += m[ind]
            ind += 1
            result +=m[-ind]

        if(len(mat)%2):
            result -= mat[len(mat)//2][len(mat)//2]
        
        return result
