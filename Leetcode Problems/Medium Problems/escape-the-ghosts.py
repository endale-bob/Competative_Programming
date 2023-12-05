class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        targetDist = abs(target[0]) + abs(target[1])
        
        for ghost in ghosts:
            ghostDist = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1]) 
            if(ghostDist <= targetDist):
                return False
            
        return True

