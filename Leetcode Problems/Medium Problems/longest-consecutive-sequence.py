class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = set(nums)
        result = 0

        seen = set()

        for num in nums:
            if(num in seen):
                continue
            seen.add(num)
            counter = 1
            left, right = 1, 1
            while(num - left in store or num + right in store):
                if(num - left in store): 
                    left += 1
                    counter += 1
                    seen.add(num-left)
                if(num + right in store): 
                    right += 1
                    counter += 1
                    seen.add(num+right)
            result = max(result, counter)
        
        return result

        
