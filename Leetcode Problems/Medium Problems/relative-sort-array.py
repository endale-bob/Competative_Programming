class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = [0]*len(arr1)
        store = defaultdict(int)
        
        for ele in arr1:
            store[ele] += 1
        
        ind = 0
        for ele in arr2:
            for value in range(store[ele]):
                result[ind] = ele
                ind += 1
            del store[ele]

        for ele in sorted(store):
            for value in range(store[ele]):
                result[ind] = ele
                ind += 1
        
        return result