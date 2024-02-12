# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None): return head

        evenp = ListNode()
        oddp = ListNode()
        tempEven = evenp
        tempOdd = oddp
        
        node = head
        ind = 1
        while(node):
            if(ind % 2 == 0):
                evenp.next = node
                evenp = evenp.next
            else:
                oddp.next = node
                oddp = oddp.next
            node = node.next
            ind += 1
        
        
        oddp.next = tempEven.next
        evenp.next = None
        
        return head


