class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = size(s)-1;
        while(l != r){
            cout << l;
            cout << "\n";
            cout << r;
            cout << "\n";
            if(l >= r){
                return true;
            }
            if(!isalnum(s[l])){
                l++;
                continue;
            }
            if(!isalnum(s[r])){
                r--;
                continue;
            }
            if(tolower(s[l]) != tolower(s[r])){
                return false;
            }
            else{
                l++;
                r--;
            }
        }
        return true;
    }
};
