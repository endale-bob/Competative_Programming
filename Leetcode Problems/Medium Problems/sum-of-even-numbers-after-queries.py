class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        ans = []
        sums = sum([num for num in nums if num%2 == 0])

        for query in queries:
            temp = nums[query[1]]
            nums[query[1]] += query[0]
            if(temp%2 == 0):
                sums -= temp
            if(nums[query[1]]%2 == 0):
                sums += nums[query[1]]
            ans.append(sums)
            # print(sums)

        return ans