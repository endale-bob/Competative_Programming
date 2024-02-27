class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        left, right = 0, len(s)-1
        while(left < right):
            if(s[right] == '1'):
                right -= 1
            elif(s[left] == '0'):
                left += 1
            else:
                ans += right - left
                right -= 1
                left += 1

        return ans
