class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        int lowest = prices[0];
        for(int i = 1; i<prices.size(); i++){
            res = max(res, prices[i]-lowest);
            lowest = min(lowest,prices[i]);
        }
        return res;
    }
};
