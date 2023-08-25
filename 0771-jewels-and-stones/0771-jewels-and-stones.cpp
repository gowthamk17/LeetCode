class Solution {
public:
    int numJewelsInStones(string jewels, string stones) {
        std::unordered_map<char, int> stoneMap;
        for(int i = 0; i < stones.size(); i++) {
            char stone = stones[i];
            if(stoneMap.find(stone) != stoneMap.end()) {
                stoneMap[stone]++;
            } else {
                stoneMap[stone] = 1;
            }
        }
        int numberOfJewelStones = 0;
        for(int i = 0; i < jewels.size(); i++) {
            char jewel = jewels[i];
            numberOfJewelStones += stoneMap[jewel];
        }
        return numberOfJewelStones;
    }
};