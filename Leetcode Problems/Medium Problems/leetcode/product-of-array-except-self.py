class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prePro = nums.copy()
        postPro = nums.copy()
        res = []

        for ind in range(1, len(nums)):
            prePro[ind] *= prePro[ind-1]
            postPro[len(nums) - ind - 1] *= postPro[len(nums) - ind]

        for ind in range(len(nums)):
            if ind == 0:
                res.append(postPro[1])
            elif ind == len(nums) -1:
                res.append(prePro[-2])
            else:
                res.append(prePro[ind - 1] * postPro[ind + 1])

        
        return res