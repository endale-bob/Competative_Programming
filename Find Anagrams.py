class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target, result = defaultdict(int), []
        if(len(p) > len(s)): return result

        for ch in p: target[ch] += 1

        for i in range(len(p) - 1):
            if s[i] in target: target[s[i]] -= 1
            
        
        for i in range(-1, len(s) - len(p) + 1):
            if(i > -1 and s[i] in target):
                target[s[i]] += 1
            if(i + len(p) < len(s) and s[i + len(p)] in target):
                target[s[i + len(p)]] -= 1
            
            if(all(v == 0 for v in target.values())):
                result.append(i +1)
        
        return result

            

