class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store = {}
        res = []

        for i in range(len(nums2)):
            store[nums2[i]] =  i;

        for i in range(len(nums1)):
            res.append(-1)
            for j in range(store[nums1[i]], len(nums2)):
                if(nums2[j] > nums1[i]):
                    res[i] = nums2[j]
                    break
                
        return res;

