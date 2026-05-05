class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int out = 0;
        stack<pair<int,int>> s;
        s.push({0,heights[0]});
        int size = heights.size();
        for(int i = 0; i < heights.size(); i++){
            int start = i;
            while(!s.empty() && heights[i] < s.top().second){
                out = std::max(out, (s.top().second)*(i-s.top().first));
                start = s.top().first;
                s.pop();
            }
            s.push({start,heights[i]});

        }
        while(!s.empty()){
            out = std::max(out, (s.top().second)*(size-s.top().first));
            s.pop();
        }
        return out;
    }
};
