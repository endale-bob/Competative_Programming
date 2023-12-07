class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = [nums[ind] for ind in range(len(nums)) if(nums[ind] > 0)]
        negative = [nums[ind] for ind in range(len(nums)) if(nums[ind] < 0)]

        result = []

        for num1, num2 in zip(positive, negative):
            result.append(num1)
            result.append(num2)

        return result
