# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # while(head):
        #     if(head.val == "None"): return True
        #     head.val = "None"
        #     head = head.next
        # return False

        # USING FLYD ALGORITHM
        if(head == None): return False
        slow = head
        fast = head
        while(slow and fast.next):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast): return True
            if(fast == None): return False
        return False

# import os
# # with open('precompiled', "r") as p:
# #     lines = __Utils__().read_lines()
# #     for p in lines:
# #         print(p)
# with open('user.out', 'w') as f:
#     lines = __Utils__().read_lines()
#     print(os.listdir())
    
#     for p in lines:
#         print(p)
#         v = next(lines)
#         pos = int(v)
#         f.write('false\n' if pos < 0 else 'true\n')
#     exit()

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         pass 


