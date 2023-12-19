class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        store = defaultdict(int)

        for domain in cpdomains:
            splitted = domain.split(" ")
            while(splitted[1]):
                store[splitted[1]] += int(splitted[0])
                ind = splitted[1].find(".") + 1
                if(ind == 0):
                    break
                splitted[1] = splitted[1][ind:] 
        print(store.items())
            
        return [str(value) +" " + key  for key, value  in store.items()]