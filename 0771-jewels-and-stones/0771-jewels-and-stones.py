class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stone_dict = {}
        for stone in stones:
            if stone in stone_dict:
                stone_dict[stone] += 1
            else:
                stone_dict[stone] = 1
        number_of_jewel_stones = 0
        for jewel in jewels:
            if jewel in stone_dict:
                number_of_jewel_stones += stone_dict[jewel]
        return number_of_jewel_stones