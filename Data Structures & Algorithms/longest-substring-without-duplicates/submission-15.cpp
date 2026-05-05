class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0;
        int l = 0;
        unordered_map<char,int> map;
        for(int i = 0; i < s.size() ; i++){
            if(map.find(s[i]) != map.end()){
                cout << "a ";
                l = max(l,map[s[i]]);
            }
            else{
                cout << "b ";
            }
            map[s[i]] = i+1;
            res = max(res,i-l+1);
                        cout << l << " "<<i << " "<< res<< "\n";
        }
        return res;
    }
};
