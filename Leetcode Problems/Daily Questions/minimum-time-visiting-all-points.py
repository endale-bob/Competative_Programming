class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        result = 0
        start = points[0]

        for point in points:
            while(start[0] != point[0] or start[1] != point[1]):
                diff1 = point[0] - start[0]
                diff2 = point[1] - start[1]
                if(start[0] != point[0] and start[1] != point[1]):
                    start[0] += 1 * (diff1/abs(diff1)) 
                    start[1] += 1 * (diff2/abs(diff2)) 
                elif(start[0] != point[0]):
                    start[0] += 1 * (diff1/abs(diff1))
                else:
                    start[1] += 1 * (diff2/abs(diff2))

                result += 1
        
        return result

