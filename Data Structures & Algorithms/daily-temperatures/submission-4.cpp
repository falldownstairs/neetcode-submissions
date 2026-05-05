class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
    vector<int> output;
    for(int i = 0; i<temperatures.size();i++){
        for(int j = i; j<temperatures.size();j++){
            if(temperatures[j]>temperatures[i]){
                output.push_back(j-i);
                break;
            }
            if(j==temperatures.size()-1){
                output.push_back(0);
                cout << i;
                cout << j;
                break;
            }
            

        }
        
    }
    return output;
    }
};
