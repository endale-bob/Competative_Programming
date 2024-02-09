class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        preSum = [0]*n

        for start, end, seats in bookings:
            preSum[start-1] += seats
            if end < n : preSum[end] -= seats

        for ind in range(1, len(preSum)):
            preSum[ind] += preSum[ind - 1]
        
        return preSum