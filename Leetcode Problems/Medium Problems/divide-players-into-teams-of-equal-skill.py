class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        total = skill[0] + skill[-1]
        chem = 0

        for i in range(len(skill)//2):
            if(total != skill[i] + skill[len(skill) - i - 1]):
                return -1
            else:
                chem += skill[i] * skill[len(skill) - i - 1]
        
        return chem


