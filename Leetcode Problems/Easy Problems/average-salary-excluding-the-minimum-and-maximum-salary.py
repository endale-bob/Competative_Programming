class Solution:
    def average(self, salary: List[int]) -> float:
        minSalary = min(salary)
        maxSalary = max(salary)

        sum = 0
        for s in salary:
            if(s != minSalary and s!= maxSalary):
                sum += s
        
        return sum/(len(salary) - 2)
        