class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size(); 
        std::unordered_map<int, int> umap;  
        for (int i = 0; i < n; i++) {
            umap[nums[i]]++;
        }
        vector<vector<int>> bucket(n+1);
        for(auto it = umap.begin(); it != umap.end(); ++it) {
            bucket[it->second].push_back(it->first);
        }
        std::vector<int> topKFreq;
        for(int i = n; i >= 0; --i) {
            if(topKFreq.size() >= k) break;
            if(!bucket[i].empty()){
                topKFreq.insert(topKFreq.end(), bucket[i].begin(), bucket[i].end());
            }
        }
        return topKFreq;
    }
};