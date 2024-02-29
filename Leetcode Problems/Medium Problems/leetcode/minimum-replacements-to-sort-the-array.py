class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        max_ele = float('inf')
        op = 0

        while len(nums) > 0 :
            curr = nums.pop()
            if curr > max_ele:

                # to know the operations
                temp_op = math.ceil(curr/max_ele) - 1
                op +=  temp_op

                # to update the max
                if(mod == 0):
                    continue
                max_ele = math.floor(curr/(temp_op+1))
                
            else:
                max_ele = curr
        
        return op
            
   



