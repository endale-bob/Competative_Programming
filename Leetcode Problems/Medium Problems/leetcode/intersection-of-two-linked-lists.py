# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        setA = set()
        setB = set()

        while(headA or headB):
            if(headA):
                setA.add(headA)
                if(headA in setB):
                    return headA
                headA = headA.next
            if(headB):
                setB.add(headB)
                if headB in setA:
                    return headB
                headB = headB.next
            
        

