# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], val = 0) -> int:
        if(root == None):
            return val

        val = (val*10) + root.val
        temp = 0

        if(root.left): temp += self.sumNumbers(root.left, val)
        if(root.right): temp += self.sumNumbers(root.right, val)

        return temp or val
        

