class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> result;
        vector<int> prevRow = {1};
        result.push_back(prevRow);
        numRows--;
        while(numRows) {
            vector<int> curRow = {1};
            if(prevRow.size() > 1) {
                for(int i = 0; i < prevRow.size() - 1; i++) {
                    int adjSum = prevRow[i] + prevRow[i+1];
                    curRow.push_back(adjSum);
                }
            }
            curRow.push_back(1);
            result.push_back(curRow);
            prevRow = curRow;
            numRows--;
        }
        return result;
    }
};