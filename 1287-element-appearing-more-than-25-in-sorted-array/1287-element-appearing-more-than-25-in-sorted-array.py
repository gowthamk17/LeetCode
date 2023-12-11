class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        arr_map = defaultdict(int)
        quater = len(arr)/4
        for n in arr:
            arr_map[n] += 1
        for key, value in arr_map.items():
            if value > quater:
                return key
        return -1