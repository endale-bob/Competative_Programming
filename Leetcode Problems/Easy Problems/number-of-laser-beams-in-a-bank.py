class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        curr = 0

        for row in bank:
            count = Counter(row)
            if(count["1"] == 0):
                continue
            else:
                result += curr*count["1"]
                curr = count["1"]
        
        return result