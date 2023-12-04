class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        result = 0
        store = capacity
        for ind in range(len(plants)):
            result += 1
            store -= plants[ind]
            if(ind + 1 < len(plants) and plants[ind +1] > store):
                result += (ind+1)*2
                store = capacity
        
        return result