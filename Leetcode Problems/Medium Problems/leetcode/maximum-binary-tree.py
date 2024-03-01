# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if(not nums):
            return        
        
        def rec(left, right):
            if(left == right):
                return
            max_ind = left
            for ind in range(left, right):
                if(nums[ind] > nums[max_ind]):
                    max_ind = ind
            curr = TreeNode(nums[max_ind])
            curr.left = rec(left, max_ind)
            curr.right = rec(max_ind+1, right)

            return curr
        
        return rec(0, len(nums))
        
        

            