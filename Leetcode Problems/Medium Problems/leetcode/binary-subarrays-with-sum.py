class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        pre = defaultdict(int)
        sums = 0
        res = 0
        pre[0] = 1

        for num in nums:
            sums += num
            res += pre[sums - k]
            pre[sums] += 1
        
        return res