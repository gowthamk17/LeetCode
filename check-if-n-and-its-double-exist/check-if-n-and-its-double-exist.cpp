class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        if(arr.size() == 0) return false;
        
        for(int i = 0; i< arr.size(); i++){
            for(int j = i + 1; j< arr.size(); j++){
                if(arr[i] == arr[j] * 2 || arr[j] == arr[i] * 2){
                    return true;
                }
            }
        }
        return false;
    }
};