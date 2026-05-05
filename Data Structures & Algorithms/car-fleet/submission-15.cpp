class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int out = 1;
        vector<pair<float,float>> pairs;
        for(int i = 0; i<position.size();i++){
            pairs.push_back({position[i], speed[i]});
        }
        sort(pairs.begin(),pairs.end());
        reverse(pairs.begin(),pairs.end());

        for(auto a : pairs){
            cout << a.first;
            cout << ':';
            cout << a.second;
            cout << "\n";
        }

        stack<pair<float,float>> s;
        s.push({pairs[0].first,pairs[0].second});

        for(int i = 1; i<pairs.size();i++){
            auto a = s.top();
            auto b = pairs[i];
            if((target-a.first)/a.second >= (target-b.first)/b.second){
                // cout << (target-b.first);
                // cout << "\n";
                // cout << b.second;
                // cout << "\n";
                // cout << (target-b.first)/b.second;
                continue;
            }
            else{
                // cout<< (target-a.first)/a.second;
                // cout << ':';
                // cout <<(target-b.first)/b.second;
                // cout << b.first;
                // cout << ':';
                // cout << b.second;
                // cout << "\n";
                s.push({b.first,b.second});
                out++;
            }

        }
        return out;
    }
};
