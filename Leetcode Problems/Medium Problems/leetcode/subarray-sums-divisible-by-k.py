class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre = Counter(map(lambda x: x%k, accumulate(nums)))
        pre[0] += 1
        ans = 0

        for remainder in pre:
            ans += (pre[remainder] * (pre[remainder] - 1)) // 2

        print(pre)
        return ans


        