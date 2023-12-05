class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        store = {}

        for ch in "qwertyuiop":
            store[ch] = 1
        for ch in "asdfghjkl":
            store[ch] = 2
        for ch in "zxcvbnm":
            store[ch] = 3
        

        result = []

        for word in words:
            row = store[word[0].lower()]
            for ch in word:
                if(store[ch.lower()] != row):
                    break
            else: result.append(word)
        
        return result