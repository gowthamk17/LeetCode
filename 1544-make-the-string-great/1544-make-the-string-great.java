class Solution {
    public String makeGood(String s) {
        if(s.length() <= 1) {
            return s;
        }
        ArrayDeque<Character> good_stack = new ArrayDeque<>();
        good_stack.addFirst(s.charAt(0));
        for(int i = 1; i < s.length(); i++) {
            char c = s.charAt(i);
            if(Character.isLowerCase(c)) {
                if(!good_stack.isEmpty() && Character.toUpperCase(c) == good_stack.peekFirst()) {
                    good_stack.removeFirst();
                } else {
                    good_stack.addFirst(c);
                }
            } else {
                if(!good_stack.isEmpty() && Character.toLowerCase(c) == good_stack.peekFirst()) {
                    good_stack.removeFirst();
                } else {
                    good_stack.addFirst(c);
                }
            }
        }
        StringBuilder good_string = new StringBuilder();
        for(char c : good_stack) {
            good_string.append(c);
        }
        return good_string.reverse().toString();
    }
}