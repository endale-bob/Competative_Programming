class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def rec(ind, sums, temp):
            # print(ind, sums, temp)
            if(len(temp) == k):
                if(sums == n):
                    ans.append(temp[:])
                return 
            if(ind > 9):
                return

            temp.append(ind)
            rec(ind+1, sums +ind, temp)
            temp.pop()
            rec(ind+1, sums, temp)
        
        rec(1, 0, [])
        return ans


