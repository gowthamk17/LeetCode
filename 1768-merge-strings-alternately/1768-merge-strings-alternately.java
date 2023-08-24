class Solution {
    public String mergeAlternately(String word1, String word2) {
        String mergedString = "";
        int mergeLimit = Math.min(word1.length(), word2.length());
        for(int i = 0; i < mergeLimit; i++) {
            mergedString += word1.charAt(i);
            mergedString += word2.charAt(i);
        }
        if(word1.length() >= mergeLimit) {
            mergedString += word1.substring(mergeLimit);
        }
        if(word2.length() >= mergeLimit) {
            mergedString += word2.substring(mergeLimit);
        }
        return mergedString;
    }
}