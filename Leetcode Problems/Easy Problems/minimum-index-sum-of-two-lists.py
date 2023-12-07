class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_elements = set.intersection(set(list1), set(list2))
        store1 = {list1[ind]:ind for ind in range(len(list1)) }
        store2 = {list2[ind]:ind for ind in range(len(list2)) }


        result = []
        current_value = None

        for ele in common_elements:
            if(not result or store1[ele] + store2[ele] < current_value):
                result.clear()
                result.append(ele)
                current_value = store1[ele] + store2[ele]
            elif(result and store1[ele] + store2[ele] == current_value):
                result.append(ele)

        return result
        


