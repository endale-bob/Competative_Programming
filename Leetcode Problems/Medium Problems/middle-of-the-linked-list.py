# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # middle = head
        # mdl = 1
        # element = 1
        # while(head.next != None):
        #     element += 1
        #     head = head.next
        #     temp = element//2 + 1
        #     if(mdl < temp):
        #         middle = middle.next
        #         mdl += 1
        # return middle

        # Two pointer
        p1 = head
        p2 = head

        while(p1 and p1.next):
            p1 = p1.next.next
            p2 = p2.next
        return p2


