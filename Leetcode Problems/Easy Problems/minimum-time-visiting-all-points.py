class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0

        for ind in range(1, len(points)):
            result += max(abs(points[ind][0] - points[ind-1][0]), abs(points[ind][1] - points[ind-1][1]))
            
        
        return result

