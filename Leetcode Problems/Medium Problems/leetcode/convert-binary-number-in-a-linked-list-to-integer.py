# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        temp = head
        ind = 0
        res = 0

        while temp.next:
            temp = temp.next
            ind += 1
        
        while head:
            res += (2**ind)*head.val
            head = head.next
            ind -= 1

        return res