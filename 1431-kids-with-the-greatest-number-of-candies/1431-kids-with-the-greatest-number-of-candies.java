class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int maxCandy = 0;
        for(int i = 0; i < candies.length; i++) {
            if(maxCandy < candies[i]) {
                maxCandy = candies[i];
            }
        }
        List<Boolean> kidList = new ArrayList<>();
        for(int i = 0; i < candies.length; i++) {
            if(candies[i] + extraCandies >= maxCandy) {
                kidList.add(true);
            } else {
                kidList.add(false);
            }
        }
        return kidList; 
    }
}