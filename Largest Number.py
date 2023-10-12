class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            return int(str(y) + str(x)) - int(str(x) + str(y))
        nums = sorted(nums, key = cmp_to_key(compare))
        return "".join(str(num) for num in nums)
