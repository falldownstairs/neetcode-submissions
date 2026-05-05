class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int longest = 0;
        unordered_set<int> numSet(nums.begin(), nums.end());
        for(int n : nums){
            int consecutive = 1;
            if(numSet.find(n - 1) == numSet.end()){
                while(numSet.find(n + consecutive) != numSet.end()){
                    consecutive++;
                }
            }
            longest = max(longest, consecutive);
        }
        return longest;
    }
};
