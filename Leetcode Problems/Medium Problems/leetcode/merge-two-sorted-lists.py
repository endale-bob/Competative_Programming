# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode()
        head = root
        while(list1 != None or list2 != None):
            if(list1 == None):
                root.next = list2
                break
            elif(list2 == None):
                root.next = list1
                break
            else:
                if(list1.val > list2.val):
                    temp = list2
                    list2 = list2.next
                else:
                    temp = list1
                    list1 = list1.next

                temp.next = None
                root.next = temp
                root = root.next
        return head.next
            
