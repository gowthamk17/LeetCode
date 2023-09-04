class Solution {
public:
    string reverseVowels(string s) {
        string vowels = "aeiouAEIOU";
        int left = 0;
        int right = s.length() - 1;
        while (left <= right)
        {
            while (left <= right && vowels.find(s[left]) == string::npos)
            {
                left++;
            }
            while (left <= right && vowels.find(s[right]) == string::npos)
            {
                right--;
            }
            if (left <= right)
            {
                char temp = s[left];
                s[left] = s[right];
                s[right] = temp;
                left++;
                right--;
            }
        }
        return s;
    }
};