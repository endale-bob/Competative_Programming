class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []

        def flipArray(k):
            left, right = 0, k
            while(left < right):
                arr[left], arr[right] = arr[right], arr[left]
                left +=1
                right -= 1

        
        while(n > 0):
            ind = arr.index(n) 
            if(ind):
                flipArray(ind)
                result.append(ind + 1)
            flipArray(n-1)
            result.append(n)
            n -= 1

        
        
        return result

        # 3 2 4 1
        # 4 2 3 1
        # 1 3 2 4


