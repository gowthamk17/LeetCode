class Solution {
public:
    int compress(vector<char>& chars) {
            string compressed = "";
            char c = chars[0];
            int count = 0;
            for(int i = 0; i < chars.size(); i++) {
                if(chars[i] == c) {
                    count++;
                }
                else {
                    compressed += c;
                    if(count > 1) {
                        compressed += to_string(count);
                    }
                    c = chars[i];
                    count = 1;
                }
            }
            compressed += c;
            if(count > 1) {
                compressed += to_string(count);
            }
            for(int i = 0; i < compressed.size(); i++) {
                chars[i] = compressed[i];
            }
            return compressed.size();
    }
};