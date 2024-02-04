class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #Simple-Approach (Sliding Window)
        #Runtime:42ms 
        lis=[]
        for i in range(0,len(blocks)):
            count_b=blocks[i:i+k].count("B")  #Count Blacks
            if(count_b>=k):                   #If Count Blacks > desired number of consecutive black blocks return 0
                return 0
            lis.append(k-count_b)       # Minimum number of operation required for consecutive black k times
        return min(lis)  #Return minimum number of blocks operation required 