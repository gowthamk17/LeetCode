class Solution {
    public String mergeAlternately(String word1, String word2) {
        StringBuilder mergedString = new StringBuilder();
        int m = word1.length();
        int n = word2.length();
        int i = 0;
        int j = 0;
        while(i < m || j < n) {
            if(i < m) {
                mergedString.append(word1.charAt(i));
                i++;
            }
            if(j < n) {
                mergedString.append(word2.charAt(j));
                j++;
            }
        }
        return mergedString.toString();
        
        // Intuition
        // String mergedString = "";
        // int mergeLimit = Math.min(word1.length(), word2.length());
        // for(int i = 0; i < mergeLimit; i++) {
        //     mergedString += word1.charAt(i);
        //     mergedString += word2.charAt(i);
        // }
        // if(word1.length() >= mergeLimit) {
        //     mergedString += word1.substring(mergeLimit);
        // }
        // if(word2.length() >= mergeLimit) {
        //     mergedString += word2.substring(mergeLimit);
        // }
        // return mergedString;
    }
}