# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        res = []
        root = head
        while(root):
            n += 1
            root = root.next

        ele_num = n/k
        remainder = n%k
        next_ = head
        for idx in range(k):
            res.append(next_)
            count = 1
            while(next_ and count < ele_num):
                next_ = next_.next
                count += 1
            remainder -= 1
            if(remainder == 0):
                ele_num = int(ele_num)
            temp = next_
            next_ = next_.next if next_ else None
            if(temp): temp.next = None
        
        return res
