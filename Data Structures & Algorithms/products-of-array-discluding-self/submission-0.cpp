class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> output;
        int numsProduct = 1;
        int zeroCounter = 0;
        for(int& n: nums){
            if(n == 0){
                zeroCounter += 1;
            }
            else{
                numsProduct *= n;
            }
        }
        if(zeroCounter == 0){
            for(int& n: nums){
                output.push_back(numsProduct/n);
            }
        }
        else if(zeroCounter == 1){
            for(int& n: nums){
                if(n == 0){
                    output.push_back(numsProduct);
                }
                else{
                    output.push_back(0);
                }
            }
        }
        else{
            for(int& _: nums){
                output.push_back(0);
            }
        }
        return output;
    }
};
