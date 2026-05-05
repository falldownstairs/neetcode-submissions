class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        for(int i = 0; i<nums.size(); i++){
            for(int j = 0; j<nums.size(); j++){
                if(nums[i] == nums[j] && i != j){
                    cout << to_string(nums[i]) + " " + to_string(nums[j]) + "\n";
                    cout << to_string(i) + " " + to_string(j) + "\n";
                    return true;
                }
            }
        }
        return false;
    }
};