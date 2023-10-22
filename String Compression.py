class Solution:
    def compress(self, chars: List[str]) -> int:
        l, r, result = 0, 0, 0
        counter, tempInd = 0, 0
        while(l < len(chars)):
            if(r < len(chars) and chars[l] == chars[r] ):
                r += 1
                counter += 1
            else:
                chars[tempInd] = chars[l] 
                counter = str(counter)
                if(int(counter) > 1):
                    result += len(counter)
                    for ch in counter:
                        tempInd = tempInd + 1
                        chars[tempInd] = ch

                tempInd += 1
                result += 1
                l = r
                counter = 0
                
        return result
                
            


