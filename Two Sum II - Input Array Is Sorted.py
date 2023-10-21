class Solution:
    def binarySearch(self, numbers, target: int, start: int) -> int:
            end = len(numbers) - 1
            middle = (start + end) // 2
            while(start < end - 1):
                if(numbers[middle] == target):
                    return middle
                elif(numbers[middle] > target):
                    end = middle
                elif(numbers[middle] < target):
                    start = middle
                middle = (start + end) // 2
            if(numbers[start] == target):
                return start
            elif(numbers[end] == target):
                return end
            return -inf

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for ind in range(len(numbers) - 1):
        #     binarySearch = self.binarySearch(numbers, target - numbers[ind], ind+1) +1
        #     if(binarySearch != -inf):
        #         return [min(ind +1, binarySearch), max(ind + 1, binarySearch)]

        store = defaultdict(int)

        for ind in range(len(numbers)):
            store[numbers[ind]] = ind
        
        for ind in range(len(numbers)):
            ind2 = store[target - numbers[ind]]
            if(ind2 > 0):
                return [min(ind +1, ind2+1), max(ind + 1, ind2+1)]
                


