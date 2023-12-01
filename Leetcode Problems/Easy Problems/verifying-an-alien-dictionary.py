class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict = {order[ind]: ind for ind in range(len(order))}
        orderDict["--"] = float("-inf")

        left, right = 0, 1
        def compare(w1, w2):
            for ind in range(max(len(w1), len(w2))):
                temp1 = w1[ind] if ind < len(w1) else "--"
                temp2 = w2[ind] if ind < len(w2) else "--"
                if(orderDict[temp2] < orderDict[temp1]):
                    return 1
                elif(orderDict[temp2] > orderDict[temp1]):
                    return -1
            return 0

        new = sorted(words, key=cmp_to_key(compare))

        for ind in range(len(words)):
            if(words[ind] != new[ind]):
                return False
        return True


