class Solution {
public:
    string reverseWords(string s) {
            int i = 0, j = 0;
            size_t size = s.length();
            vector<string> arr;
            while(i < size)
            {
                while(i < size && s[i] == ' ')
                {
                    i++;
                }
                j = i;
                while(j < size && s[j] != ' ')
                {
                    j++;
                }
                if(i < size) 
                {
                    arr.push_back(s.substr(i,j-i));
                }
                i = j;
            }
            reverse(arr.begin(), arr.end());
            s = "";
            for(const string &str: arr)
            {
                s+=(str + ' ');
            }
            s.erase(s.size() - 1);
            return s;
    }
};