class Solution {
    public int characterReplacement(String s, int k) {
        HashMap<Character, Integer> countMap = new HashMap<>();
        int result = 0;
        int left = 0;
        int maxf = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);
            int count = countMap.getOrDefault(c, 0);
            countMap.put(c, count+1);
            maxf = Math.max(maxf, countMap.get(c));
            if(((right-left+1) - maxf) > k) {
                countMap.put(s.charAt(left), countMap.get(s.charAt(left))-1);
                left++;
            }
            result = Math.max(result, right-left+1);
        }
        return result;
    }
}