class Solution:
    def frequencySort(self, s: str) -> str:
        dict1 = Counter(s)
        dict1 = sorted(dict1.items(), key = lambda item: item[1], reverse = True)
        newstr = "".join(i[0]*i[1] for i in dict1)
        return newstr
