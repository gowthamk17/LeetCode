class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        re_dict = {}
        for string in list1:
            if string in list2:
                re_dict[string] = list1.index(string) + list2.index(string)
        i = list(sorted(re_dict.values()))[0]
        result = [k for k,v in re_dict.items() if v == i]            
        return result