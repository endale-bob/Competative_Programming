class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ptr1, ptr2 = 0, 0
        # firstList.append([inf, inf])
        # secondList.append([inf, inf])
        result = []

        while(ptr1 < len(firstList) and ptr2 < len(secondList)):
            if(firstList[ptr1][0] <= secondList[ptr2][0] <= firstList[ptr1][1]):
                result.append([secondList[ptr2][0], min(secondList[ptr2][1], firstList[ptr1][1])])
            elif(secondList[ptr2][0] <= firstList[ptr1][0] <= secondList[ptr2][1]):
                result.append([firstList[ptr1][0], min(secondList[ptr2][1], firstList[ptr1][1])])

            if(secondList[ptr2][1] > firstList[ptr1][1]):
                ptr1 += 1
            else:
                ptr2 += 1
        # result.pop()
        
        return result
