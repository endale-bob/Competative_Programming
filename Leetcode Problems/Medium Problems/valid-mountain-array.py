class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if(len(arr) < 3): return False
        sign = -1

        for ind in range(1, len(arr)):
            if(sign > 1): return False
            if(sign <= 0):
                if(arr[ind] < arr[ind-1]):
                    if(sign == -1): return False
                    sign +=1
                elif(arr[ind] == arr[ind-1]):
                    return False
                elif(sign == -1): sign = 0
            elif(sign == 1):
                if(arr[ind] > arr[ind-1]):
                    sign +=1
                elif(arr[ind] == arr[ind-1]):
                    return False
        
        return sign == 1
        

        
        
        return True