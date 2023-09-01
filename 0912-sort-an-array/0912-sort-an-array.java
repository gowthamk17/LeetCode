class Solution {
    public int[] sortArray(int[] nums) {
        int minVal = 0;
        int maxVal = 0;
        HashMap<Integer, Integer> countMap = new HashMap<>();
        for(int n : nums) {
            if(minVal > n) {
                minVal = n;
            } else if(maxVal < n) {
                maxVal = n;
            }
            countMap.put(n, countMap.getOrDefault(n,0)+1);
        }
        int i = 0;
        while(minVal <= maxVal) {
            if(countMap.containsKey(minVal)) {
                int times = countMap.get(minVal);
                while(times != 0) {
                    nums[i] = minVal;
                    i++;
                    times--;
                }
            }
            minVal++;
        }
        return nums;
    }
}