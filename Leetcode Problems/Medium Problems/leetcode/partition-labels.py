class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        store = defaultdict(lambda : -1)

        for i in range(0, len(s)):
            store[s[i]] = i
        
        lst = []
        max_ind = 0
        end = 0
        for ind in range(len(s)):
            max_ind = max(store[s[ind]], max_ind)
            if(max_ind == ind):
                lst.append(ind + 1 - end)
                end = ind + 1
                max_ind = 0

        return lst
