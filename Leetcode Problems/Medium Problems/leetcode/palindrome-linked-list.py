# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        high = head
        mid = head
        stack = []
        while(high and high.next):
            stack.append(mid.val)
            high = high.next.next
            mid = mid.next
            
        if(high != None): mid = mid.next

        while(mid):
            if(mid.val != stack.pop()): return False
            mid = mid.next
        return True
        



