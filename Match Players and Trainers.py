class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        p_ptr, t_ptr = len(players) -1, len(trainers) -1
        result = 0

        while(p_ptr >= 0 and t_ptr >= 0):
            if(trainers[t_ptr] >= players[p_ptr]):
                result += 1
                t_ptr -= 1
            p_ptr -= 1
        
        return result
            

        
