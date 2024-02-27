class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        n = len(answers)
        answers.sort()
        right = 0
        res = 0

        while(right < n):
            counter = 0
            temp = answers[right]
            while(right < n and answers[right] == temp):
                counter += 1
                right += 1
            if(temp == 0):
                res += counter
            elif(counter <= temp+1):
                res += temp+1
            elif(counter > temp):
                res += ((counter//(temp+1))*temp) + counter//(temp+1)
                if(counter%(temp+1) != 0): res += temp+1
            print(answers, right, res, counter)
        
        return res

        
        

        