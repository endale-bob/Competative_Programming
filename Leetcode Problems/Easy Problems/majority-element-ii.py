class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)//3
        store = defaultdict(float)
        result = []

        for num in nums:
            store[num] += 1
            if(store[num] > N):
                store[num] = float("-inf")
                result.append(num)

        return result