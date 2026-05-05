class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size()-1;
        vector<int> out;
        while(l<r){
            cout<< l;
            cout << "\n";
            cout << r;
            cout << "\n";
            int sum = numbers[l] + numbers[r];
            if(sum == target){
                out.push_back(l+1);
                out.push_back(r+1);
                return out;
            }
            else if(sum > target){
                r--;
            }
            else{
                l++;
            }
        }
        return out;
    }
};
