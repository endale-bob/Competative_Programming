class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        psum = [0] * len(s)
        res = [ord(c) - 97 for c in s]

        for shift in shifts:
            psum[shift[0]] += 1 if shift[2] == 1 else -1
            if(shift[1] +1 < len(s)):
                psum[shift[1]+1] -= 1 if shift[2] == 1 else -1
        
        for i in range(1, len(s)):
            psum[i] += psum[i-1]
        
        for i in range(len(s)):
            res[i] += psum[i]
            res[i] %= 26
        
        return "".join([chr(num + 97) for num in res])
        
