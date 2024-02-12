# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        greaterNodes = ListNode("dummy")
        lessNodes = ListNode("dummy")
        greatHolder = greaterNodes
        lessHolder = lessNodes
        temp = head

        while(temp):
            if temp.val >= x:
                greaterNodes.next = temp
                greaterNodes = greaterNodes.next
            else:
                lessNodes.next = temp
                lessNodes = lessNodes.next
            temp = temp.next
        
        lessNodes.next = greatHolder.next
        greaterNodes.next = None

        return lessHolder.next