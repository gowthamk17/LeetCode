class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_val = -1
        max_val = -1
        count_map = {}
        for n in nums:
            if n < min_val:
                min_val = n
            elif n > max_val:
                max_val = n
            count_map[n] = count_map.get(n,0) + 1
        arr = []
        for n in range(min_val, max_val+1):
            if n in count_map:
                while count_map[n] != 0:
                    arr.append(n)
                    count_map[n] -= 1
        return arr