class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int out = 0;
        for(int i = 0; i< heights.size(); i++){
            int min = i;
            int max = i;
            if(i != heights.size()-1){
                for(int j = i+1; j<heights.size(); j++){
                    if(heights[j]>=heights[i]){
                        max++;
                    }
                    else{
                        break;
                    }
                }
            }
            if(i != 0){
                for(int j = i-1; j>=0; j--){
                if(heights[j]>=heights[i]){
                    min--;
                }
                else{
                    break;
                }
            }
            }
            int rect = (heights[i]*(max-min+1));
            cout << rect;
            cout << "\n";
            out = std::max(out, rect);

        }
        return out;
    }
};
