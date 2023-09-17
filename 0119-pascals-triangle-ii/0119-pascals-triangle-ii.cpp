class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> row = {1};
        if(rowIndex == 0) return row;
        while(rowIndex--) {
            vector<int> prevRow = {0};
            prevRow.insert(prevRow.end(), row.begin(), row.end());
            prevRow.push_back(0);
            
            row.clear();
            for(int i = 0; i < prevRow.size() - 1; i++) {
                row.push_back(prevRow[i] + prevRow[i+1]);
            }
        }
        return row;
    }
};