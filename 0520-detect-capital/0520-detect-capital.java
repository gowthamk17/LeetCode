class Solution {
    public boolean detectCapitalUse(String word) {
        if (word.length() == 1) {
                return true;
        }
        if (Character.isUpperCase(word.charAt(0))) {
            if(Character.isUpperCase(word.charAt(1))) {
                if(isAllUpper(word.substring(1))) {
                    return true;
                }
                else {
                    return false;
                }
            }
            else {
                if(isAllLower(word.substring(1))) {
                    return true;
                }
            }
        }  
        else {
            if(isAllLower(word.substring(1))) {
                return true;
            }
            else {
                return false;
            }
        }
        return false;
    }
    
    public static boolean isAllUpper(String str) {
        for (int i = 0; i < str.length(); i++) {
            if (!Character.isUpperCase(str.charAt(i))) {
                return false;
            }
        }
        return true;
    }

    public static boolean isAllLower(String str) {
        for (int i = 0; i < str.length(); i++) {
            if (!Character.isLowerCase(str.charAt(i))) {
                return false;
            }
        }
        return true;
    }
}