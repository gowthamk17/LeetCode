class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int maxCandy = 0;
        for(int candy : candies) {
            if(maxCandy < candy) {
                maxCandy = candy;
            }
        }
        List<Boolean> kidList = new ArrayList<>();
        for(int candy : candies) {
            if(candy + extraCandies >= maxCandy) {
                kidList.add(true);
            } else {
                kidList.add(false);
            }
        }
        return kidList; 
    }
}