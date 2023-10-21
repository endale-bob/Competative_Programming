class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) -1
        area = 0
        while(l < r):
            w = r - l
            h = min(height[l], height[r])
            area = max(area, w*h)
            if(height[l] > h):
                r -= 1
            else:
                l += 1
        
        return area
