class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result = [0]*len(boxes)
        n = len(boxes)

        leftCount, leftCost = 0, 0
        for ind in range(1, n):
            if(boxes[ind-1] == "1"): leftCount += 1
            leftCost += leftCount
            result[ind] += leftCost
        
        rightCount, rightCost = 0, 0
        for ind in range(n-2, -1, -1):
            if(boxes[ind+1] == "1"): rightCount += 1
            rightCost += rightCount
            result[ind] += rightCost
        
        return result
