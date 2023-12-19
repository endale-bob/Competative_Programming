class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [ind+1 for ind in range(n)]
        counter = 0
        while(len(friends) > 1):
            counter = (counter + k - 1)%n
            friends.pop(counter)
            n -= 1
        
        return friends[0]

