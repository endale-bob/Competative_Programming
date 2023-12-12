class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        store = defaultdict(list)

        for path in paths:
            ind = path.rfind("/")
            temp_path = path[:ind] if ind > -1 else ""
            files = path[ind+1:].split(" ")
            temp_path = "".join([temp_path, "/", files[0]]) if temp_path else files[0]
            for i in range(1, len(files)):
                start = files[i].find("(") +1
                end = files[i].rfind(")")
                content = files[i][start: end]
                file = "".join([temp_path, "/", files[i][:start-1]]) if temp_path else files[i][:start-1]
                store[content].append(file)
        
        return [files for files in store.values() if len(files) > 1]



