class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        for ele in s:
            count[ele] += 1
        
        ans = 0
        odd = False
        for ind in count.keys():
            if(count[ind] %2 == 0):
                ans += count[ind]
            else:
                ans += count[ind] - 1
                odd = True
        
        if odd: ans += 1
        return ans
