class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        pt1, pt2 = 0, 0
        nums1.append(inf)
        nums2.append(inf)
        result = 0

        while(pt1 < len(nums1) and pt2 < len(nums2)):
            if(nums1[pt1] == nums2[pt2]):
                result = nums1[pt1]
                break
            elif(nums1[pt1] > nums2[pt2]):
                pt2 += 1
            else:
                pt1 += 1
        
        return result if result != inf else -1