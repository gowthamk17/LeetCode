class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int N = arr.size();
        int max = -1;
        if(N < 2) arr[0] = max;
        for(int i = 0; i< N; i++){
            for(int j = i+1; j< N; j++){
                if(arr[j] > max){
                    max = arr[j];
                }
            }
            arr[i] = max;
            max = -1;
        }
        return arr;
    }
};