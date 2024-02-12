# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hd = None
        while(head):
            temp = head.next
            head.next = hd
            hd = head
            head = temp
        return hd
