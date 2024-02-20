class Solution:
    def argmin(self, arr: list) -> list:
        n = len(arr)
        idx = 0
        val = float('inf')
        for ind in range(n):
            if arr[ind] < val:
                val = arr[ind]
                idx = ind
        
        return idx
        

    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        opencost = []
        for ind in range(n):
            temp = opencost[-1] if len(opencost) > 0 else 0
            if(ind > 0 and customers[ind - 1] == 'N'):
                temp = temp + 1
            opencost.append(temp)
        
        closecost = [0]*n
        for ind in range(n-1, -1, -1):
            temp = closecost[ind+1] if ind != n-1 else 0
            if(customers[ind] == 'Y'):
                temp += 1
            
            closecost[ind] = temp
        temp = opencost[-1]
        opencost.append(temp)
        # temp = 0 if customers[-1] == 'N' else opencost[-1] - 1
        closecost.append(0)

        combined = [closecost[ind] + opencost[ind] for ind in range(n+1)]
        print(combined)

        return self.argmin(combined)
