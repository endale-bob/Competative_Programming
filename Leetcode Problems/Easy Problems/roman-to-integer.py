class Solution:
    def romanToInt(self, s: str) -> int:
        left, right = 0, 2
        romanToIntDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        pairsDict = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        result = 0

        while(left < len(s)):
            if(s[left:right] in pairsDict):
                result += pairsDict[s[left:right]]
                left +=2
                right += 2
            else:
                result += romanToIntDict[s[left]]
                left+=1
                right += 1
        
        return result

        