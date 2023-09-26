class Solution {
public:
    int secondHighest(string s) {
        int first = -1, second = -1;
        for (int i = 0; s[i] != '\0'; i++)
        {
            if (isdigit(s[i]))
            {
                int n = s[i] - '0';
                if (n > first)
                {
                    second = first;
                    first = n;
                }
                else if(n > second && n != first)
                {
                    second = n;
                }
            }
        }
        return second;
    }
};