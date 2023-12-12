class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        store = defaultdict(int)
        result = [set(), set()]

        for match in matches:
            store[match[1]] += 1

            if match[1] in result[0]: 
                result[0].remove(match[1])

            if(store[match[1]] == 1):
                result[1].add(match[1])

            if(match[1] in result[1] and store[match[1]] > 1):
                result[1].remove(match[1])

            if(store[match[0]] == 0):
                result[0].add(match[0])

            
        return [sorted(list(result[0])), sorted(list(result[1]))]
