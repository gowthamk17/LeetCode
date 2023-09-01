class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = -1
        for candy in candies:
            if candy > max_candy:
                max_candy = candy
        candy_list = []
        for candy in candies:
            if candy + extraCandies >= max_candy:
                candy_list.append(True)
            else:
                candy_list.append(False)
        return candy_list