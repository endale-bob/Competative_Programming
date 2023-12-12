class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        bad = set()
        good = set()

        for front, back in zip(fronts, backs):
            if(front != back):
                if(front not in bad):
                    good.add(front)
                if(back not in bad):
                    good.add(back)
            else:
                if(front not in bad):
                    bad.add(front)
                if(front in good):
                    good.remove(front)
                if(back not in bad):
                    bad.add(back)
                if(back in good):
                    good.remove(back)

        return min(good) if len(good) > 0 else 0
