class TimeMap {
public:
    unordered_map<string, vector<pair<string,int>>> tmap;
    TimeMap() {
    }
    
    void set(string key, string value, int timestamp) {
        tmap[key].push_back({value,timestamp});
    }
    
    string get(string key, int timestamp) {
        vector<pair<string,int>> v = tmap[key];
        int l = 0; int r = v.size()-1;
        int mid;
        string res = "";
        while(l<=r){
            mid = (l+r)/2;
            int midPairSecond = v[mid].second;
            if(midPairSecond <= timestamp){
                res = v[mid].first;
                l = mid+1;
            }
            else{
                r = mid-1;
            }
        }
        return res;
    }
};

// [1,2,3,5]
// timestamp = 4
