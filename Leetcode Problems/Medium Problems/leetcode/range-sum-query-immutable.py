class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = []
        curr = 0
        for num in nums:
            self.prefix.append(num + curr)
            curr = self.prefix[-1]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right] - self.prefix[left-1] if left > 0 else self.prefix[right]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)