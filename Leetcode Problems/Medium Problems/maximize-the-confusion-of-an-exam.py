class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        answerDict = defaultdict(int)
        left, right = 0, 0
        result = 0

        while(right < len(answerKey) and left < len(answerKey)):
            answerDict[answerKey[right]] += 1
            if(answerDict["T"] > k and answerDict["F"] > k):
                answerDict[answerKey[left]] -= 1
                left += 1
                
            result = max(answerDict['T'] + answerDict['F'], result)
            right += 1

        return result                
            
