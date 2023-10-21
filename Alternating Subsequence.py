def alternatingSubsequence(n: int, nums: list):
     max_pos = 0
     min_neg = float("-inf")
     result = 0
     
     for num in nums:
        if(num > 0):
             if(min_neg != float("-inf")): 
                 result += min_neg
                 min_neg = float("-inf")
             max_pos = max(max_pos, num)
        else:
            result += max_pos
            max_pos = 0
            min_neg = max(min_neg, num)
    
     if(min_neg != float("-inf")): result += min_neg
     result +=  max_pos 
            
     print(result)
             
     

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        
        alternatingSubsequence(n, nums)
    
    
