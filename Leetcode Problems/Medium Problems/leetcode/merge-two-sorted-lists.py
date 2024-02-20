# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recSol(self, list1: Optional[ListNode], list2: Optional[ListNode], root: ListNode) -> list[ListNode]:
        if(list1 == None):
            root.next = list2
            return
        elif(list2 == None):
            root.next = list1
            return 

        if(list1.val > list2.val):
            root.next = list2
            list2 = list2.next
        else:
            root.next = list1
            list1 = list1.next
        
        root = root.next
        return self.recSol(list1, list2, root)
        
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode("dummy")
        self.recSol(list1, list2, head)

        return head.next
            
