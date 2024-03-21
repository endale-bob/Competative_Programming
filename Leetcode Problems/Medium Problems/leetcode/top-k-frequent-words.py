class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = defaultdict(int)

        for word in words:
            freq[word] += 1

        temp = sorted(freq.keys())
        return sorted(temp, key = lambda x: freq[x], reverse = True)[:k]