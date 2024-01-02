class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        store = defaultdict(int)

        for num in nums:
            store[num] += 1
        
        result = []

        while(len(store) > 0):
            temp = []
            for num in list(store.keys()):
                temp.append(num)
                store[num] -= 1
                if(store[num] <= 0):
                    del store[num]
            result.append(temp)
        
        return result

