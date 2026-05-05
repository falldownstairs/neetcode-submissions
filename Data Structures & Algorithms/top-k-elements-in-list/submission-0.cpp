class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> output;
        vector<vector<int>> freq(nums.size() + 1);
        unordered_map<int, int> elements;
        for(int n : nums){
            elements[n] = 1 + elements[n];
        }
        for(const auto& pair : elements){
            freq[pair.second].push_back(pair.first);
        }
        int c = k;
        for(int i = freq.size() - 1; i>0; i--){
            for(int n : freq[i]){
                output.push_back(n);
                c--;
                if(c == 0){
                    return output;
                }
            }
        }
        


        return output;
    }
};
