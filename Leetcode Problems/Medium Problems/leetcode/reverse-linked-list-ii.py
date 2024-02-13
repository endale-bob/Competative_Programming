# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        head = ListNode("dummy", head)
        rightNode = head
        while(right > 0 and rightNode):
            rightNode = rightNode.next
            right -= 1
        
        leftNode = head
        while(left > 1 and leftNode):
            leftNode = leftNode.next
            left -= 1
        
        while(leftNode.next != rightNode):
            temp = leftNode.next
            # remove the node
            leftNode.next = temp.next

            # insert it in reverse position
            temp.next = rightNode.next
            rightNode.next = temp
        
        return head.next




        

