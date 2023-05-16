class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
            std::unordered_map<int, int> umap;
            int numsSize = nums.size(); 
            for (int i = 0; i < numsSize; i++)
            {
                umap[nums[i]]++;
            }
            std::stack<int> arr[numsSize + 1];
            for (const auto &[key, value] : umap)
            {
                arr[value].push(key);
            }
            std::vector<int> topKFreq;
            for(int i = numsSize, j=k; i >= 0; --i) {
                while(!arr[i].empty()) {
                    topKFreq.push_back(arr[i].top());
                    arr[i].pop();
                    --j;
                    if(j == 0) break;
                }
                if(j == 0) break;
            }
            return topKFreq;
    }
};