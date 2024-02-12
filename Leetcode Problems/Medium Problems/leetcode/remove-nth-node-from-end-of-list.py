# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head = ListNode("Dummy", head)
        ptr1 = head
        ptr2 = head
        print(head)
        while (n > 0):
            ptr1 = ptr1.next
            n -= 1
        
        while(ptr1.next):
            ptr2 = ptr2.next
            ptr1 = ptr1.next
        
        ptr2.next = ptr2.next.next
        return head.next


        

