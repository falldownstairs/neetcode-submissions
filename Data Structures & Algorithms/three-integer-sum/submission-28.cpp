class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> out;
        sort(nums.begin(),nums.end());
        for(int i = 0; i<nums.size(); i++){
            if(i>0 && nums[i-1]==nums[i]){
                continue;
            }
            int l=i+1;
            int r=nums.size()-1;
            while(l<r){
                int threeSum = nums[i]+nums[l]+nums[r];
                if (threeSum>0){
                    r--;
                }
                else if(threeSum<0){
                    l++;
                }
                else{
                    vector<int> v = {nums[i],nums[l],nums[r]};
                    out.push_back(v);
                    l++;
                    r--;
                    while(nums[l] == nums[l-1] && l<r){
                        l++;
                    }
                }
            }
        }
        return out;
    }
};
