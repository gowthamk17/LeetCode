class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        HashMap<Character, Integer> stoneMap = new HashMap<>();
        for(int i = 0; i < stones.length(); i++) {
            char stone = stones.charAt(i);
            if(stoneMap.containsKey(stone)) {
                int value = stoneMap.get(stone) + 1;
                stoneMap.put(stone, value);
            } else {
                stoneMap.put(stone, 1);
            }
        }
        int numberOfJewelsInStones = 0;
        for(int i = 0; i < jewels.length(); i++) {
            char jewel = jewels.charAt(i);
            if(stoneMap.containsKey(jewel)) {
                numberOfJewelsInStones += stoneMap.get(jewel);
            }
        }
        return numberOfJewelsInStones;
    }
}