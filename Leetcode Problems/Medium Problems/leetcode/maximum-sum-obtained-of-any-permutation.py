class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        preSum = [0]* n

        for start, end in requests:
            preSum[start] += 1
            if end + 1 < n : preSum[end+1] -= 1

        preSum = list(accumulate(preSum))
        preSum.sort()
        nums.sort()
        ans = 0
        for ind in range(n) :
            ans += (preSum[ind] * nums[ind])
        
        return ans % (10**9 + 7)