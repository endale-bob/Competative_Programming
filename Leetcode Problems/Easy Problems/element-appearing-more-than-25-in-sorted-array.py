class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        freq_ele = arr[0]
        freq_num = 1
        temp_freq = 0

        for ind in range(1, len(arr)):
            if(arr[ind] != arr[ind-1]):
                temp_freq = 0
            temp_freq +=1
            if(temp_freq > freq_num):
                freq_num = temp_freq
                freq_ele = arr[ind]
            
        return freq_ele