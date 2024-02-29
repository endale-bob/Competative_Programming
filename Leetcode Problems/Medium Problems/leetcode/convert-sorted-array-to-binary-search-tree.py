# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return 
        ind = len(nums)//2
        
        res = TreeNode(nums[ind])
        left = self.sortedArrayToBST(nums[:ind])
        res.left = left
        right = self.sortedArrayToBST(nums[ind+1:])
        res.right = right

        return res