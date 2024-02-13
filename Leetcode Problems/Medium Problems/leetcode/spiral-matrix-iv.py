# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, n: int, m: int, head: Optional[ListNode]) -> List[List[int]]:
        temp = head
        res = [[0]*m for i in range(n)]
        row, col = n, m
        j = 0

        while(row > 0 and col > 0):
            print(row, col)

            for ind in range(j, m-j):
                if(temp):
                    res[j][ind] = temp.val
                    temp = temp.next
                else:
                    res[j][ind] = -1
                
                if(ind == j): row -= 1
            
            if(row == 0): break

            for ind in range(1+j, n-j):
                if(temp):
                    res[ind][-1-j] = temp.val
                    temp = temp.next
                else:
                    res[ind][-1-j] = -1
                
                if(ind == 1+j): col -= 1
            
            if(col == 0): break
            
            for ind in range(m-2 - j, -1 + j, -1):
                if(temp):
                    res[-1-j][ind] = temp.val
                    temp = temp.next
                else:
                    res[-1-j][ind] = -1
                
                if(ind == m-2 - j):row -= 1
            
            for ind in range(n-2-j, j, -1):
                if(temp):
                    res[ind][j] = temp.val
                    temp = temp.next
                else:
                    res[ind][j] = -1
                
                if(ind == n-2-j): col -= 1
            
            j+=1

        print(res)
        return res