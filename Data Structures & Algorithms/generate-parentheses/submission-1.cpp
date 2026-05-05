class Solution {
public:
    vector<string> generateParenthesis(int n) {
        string str;
        vector<string> output;
        function<void(int,int)> backtrack = [&](int open,int close){
            if(open==close && open == n){
                output.push_back(str);
                return;
            }
            if(open<n){
                str += '(';
                backtrack(open+1,close);
                str = str.substr(0,open+close);
            }
            if(close<open){
                str += ')';
                backtrack(open,close+1);
                str = str.substr(0,open+close);
            }
        };
        backtrack(0,0);
        return output;
    }
    
};
