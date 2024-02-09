class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = max(trips, key = lambda x: x[2])[2]
        preSum = [0]*n

        # [9 ]

        for num, start, end in trips:
            preSum[start] += num
            if end < n : preSum[end] -= num

        for ind in range(1, n):
            preSum[ind] += preSum[ind-1]

        max_capacity = max(preSum)

        return max_capacity <= capacity