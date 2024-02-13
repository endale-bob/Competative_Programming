# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        DummyNode = ListNode(float('-inf'), head)
        DummyNode.prev = None
        head = DummyNode

        node = head
        curr = head.next
        while(curr):
            curr.prev = node
            node = node.next
            curr = curr.next
        
        rightNode = head.next
        while(rightNode):
            leftNode = rightNode.prev
            temp = rightNode.next
            while(leftNode):
                if(leftNode.val > rightNode.val):
                 # remove the rightNode from its rightNodeent position
                    if(rightNode.next): 
                        rightNode.prev.next = rightNode.next
                        rightNode.next.prev = rightNode.prev
                    else:
                        rightNode.prev.next = None
                    
                    # add the rightNode before the leftNode
                    if(leftNode.prev):
                        leftNode.prev.next = rightNode
                        rightNode.prev = leftNode.prev
                    rightNode.next = leftNode
                    leftNode.prev = rightNode
                # else:
                #     print(leftNode.val, rightNode.val)
                #     print(head)
                #     break

                
                leftNode = leftNode.prev
            rightNode = temp

        return head.next








