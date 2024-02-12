# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        store = set()
        curr = head
        if(head == None): return head

        nxt = head.next

        while(nxt):
            store.add(curr.val)
            if(nxt.val in store):
                curr.next = nxt.next
                nxt.next = None
            else:
                curr = curr.next
            if(curr): nxt = curr.next
            else: nxt = None
            
        
        return head