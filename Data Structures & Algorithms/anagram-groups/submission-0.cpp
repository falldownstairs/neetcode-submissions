class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> output;
        unordered_map<string, int> anagrams;
        int c = 0;
        for(int i = 0; i < strs.size(); i++){
            string ref = strs[i];
            sort(ref.begin(), ref.end());
            if(anagrams.count(ref) == 0){
                anagrams[ref] = c;
                c++;
                cout << anagrams[ref];
                output.push_back({});
                output[anagrams[ref]].push_back(strs[i]);
            }
            else{
                output[anagrams[ref]].push_back(strs[i]);
            }
        }
        return output;
    }
};
