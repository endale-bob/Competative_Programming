# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def rec(left, right):
            if left == None and right == None:
                return None
            elif left == None:
                return right
            elif right == None:
                return left

            node = TreeNode(left.val + right.val)
            node.right = rec(left.right, right.right)
            node.left = rec(left.left, right.left)

            return node
        
        return rec(root1, root2)