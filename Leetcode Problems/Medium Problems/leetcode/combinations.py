class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(num1, path):
            if len(path) == k:
                ans.append(path[:])
                return 
            for num in range(num1, n+1):
                path.append(num)
                backtrack(num+1, path)
                path.pop()

        ans = []
        backtrack(1, [])
        return ans
            
