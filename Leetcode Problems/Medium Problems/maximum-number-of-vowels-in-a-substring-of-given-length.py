class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        # define my static and final variable
        vowels = {'a', 'e', 'i', 'o', 'u'}
        answer = 0

        # define the static sliding window
        for i in range(k):
            if(s[i] in vowels): answer += 1

        # find the max vowels in static sliding window
        left = 0
        current = answer
        for right in range(k, len(s)):
            if(s[right] in vowels): current += 1
            if(s[left] in vowels): current -= 1
            left +=1
            answer = max(current, answer)

        return answer
