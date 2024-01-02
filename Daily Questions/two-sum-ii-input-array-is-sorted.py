class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        store = {numbers[ind]: ind for ind in range(len(numbers))}

        for ind in range(len(numbers)):
            if(target - numbers[ind] in store):
                return [ind+1, store[target - numbers[ind]]+1 ]
         
