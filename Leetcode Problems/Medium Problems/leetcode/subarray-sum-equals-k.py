class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefSum = nums.copy()
        freq = defaultdict(int)
        
        for ind in range(1, len(nums)):
            prefSum[ind] += prefSum[ind-1]
            freq[prefSum[ind]] += 1
        
        if(len(nums) > 0): freq[prefSum[0]] += 1


        res = 0
        seen = defaultdict(int)
        for ind in range(len(nums)):
            cond = k + prefSum[ind] - nums[ind]
            if(freq[cond] > 0):
                curr = freq[cond] - seen[cond]
                res += curr
            seen[prefSum[ind]] += 1
               
        return res

