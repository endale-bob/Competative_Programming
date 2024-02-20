class Solution:
    def recSol(self, arr: list, n: int) -> list[int]:
        if(n == 0):
            return arr
        prev = arr[0]
        for ind in range(1, len(arr)):
            prev = arr[ind ] + prev
            prev, arr[ind] = arr[ind], prev
        
        arr.append(1)

        return self.recSol(arr, n -1)

    def getRow(self, rowIndex: int) -> List[int]:
        return self.recSol([1], rowIndex)

    
        