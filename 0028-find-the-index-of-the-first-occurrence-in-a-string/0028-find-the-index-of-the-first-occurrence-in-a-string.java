class Solution {
    public int strStr(String haystack, String needle) {
        if(haystack.length() < needle.length()) {
            return -1;
        }
        boolean found = false;
        for(int i = 0; i < haystack.length(); i++){
            if(haystack.charAt(i) == needle.charAt(0)) {
                int l = i;
                found = true;
                for(int j = 0; j < needle.length(); j++) {
                    if(l >= haystack.length() || haystack.charAt(l) != needle.charAt(j)) {
                        found = false;
                        break;
                    }
                    l++;
                }
                if(found) {
                    return i;
                }
            }
        }
        return -1;
    }
}