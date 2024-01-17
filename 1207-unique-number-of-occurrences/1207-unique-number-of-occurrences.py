class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_map = Counter(arr)
        val_set = set()
        for val in arr_map.values():
            if val not in val_set:
                val_set.add(val)
            else:
                return False
        return True