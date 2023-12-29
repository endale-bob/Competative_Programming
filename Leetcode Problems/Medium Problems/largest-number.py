class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def our_cmp(num1, num2):
            num1 = str(num1)
            num2 = str(num2)
            
            # for i in range(len(num1)+ len(num2)):
            #     if(num1[i%len(num1)] < num2[i%len(num2)]):
            #         return -1
            #     elif(num1[i%len(num1)] > num2[i%len(num2)]):
            #         return 1
            if(num1+num2 > num2+num1):
                return 1
            else:
                return -1


        nums.sort(key = cmp_to_key(our_cmp), reverse = True) # nlogn
        result = "".join(map(str, nums)) # n

        if result[0] == '0':
            result="0"


        return result