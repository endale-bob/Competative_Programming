class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        _store = defaultdict(int)

        for bill in bills:
            change = bill - 5
            if change == 0:
                pass
            elif change == 5 and _store[5]:
                _store[5] -= 1
            elif change == 10 and (_store[10] or _store[5] >= 2):
                if(_store[10]): _store[10] -= 1
                else: _store[5] -= 2
            elif(change == 15):
                if(_store[10] and _store[5]):
                    _store[10] -= 1
                    _store[5] -= 1
                elif(_store[5] >= 3):
                    _store[5] -= 3
                else: 
                    return False
            else:
                return False
            
            _store[bill] += 1
            print(_store)
            

        return True