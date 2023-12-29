class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        v_area = 0

        for i in range(1, len(points)):
            if(points[i][0] - points[i-1][0] > v_area):
                v_area = points[i][0] - points[i-1][0]
        
        return v_area