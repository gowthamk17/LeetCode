class Solution {
    public boolean buddyStrings(String s, String goal) {
        if(s.length() != goal.length()) {
            return false;
        }
        if(s.equals(goal)) {
            int[] freq = new int[26];
            for(char ch : s.toCharArray()) {
                freq[ch - 'a'] += 1;
                if(freq[ch - 'a'] == 2) {
                    return true;
                }
            }
            return false;
        }
        int fi = -1;
        int si = -1;
        for(int i = 0; i < s.length(); i++) {
            if(s.charAt(i) != goal.charAt(i)) {
                if(fi == -1) {
                    fi = i;
                } else if(si == -1) {
                    si = i;
                } else {
                    return false;
                }
            }
        }
        if(si == -1) {
            return false;
        }
        return s.charAt(fi) == goal.charAt(si) && s.charAt(si) == goal.charAt(fi);
    }
}