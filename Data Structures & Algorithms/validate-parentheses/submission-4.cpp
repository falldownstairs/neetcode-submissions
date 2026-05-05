class Solution {
public:
    bool isValid(string s) {
        stack<char> open;
        for(char c : s){
            if(open.empty() &&(c == '}' || c == ')' || c == ']')){
                return false;
            }
            else if(c == '}'){
                if(open.top() != '{'){
                    return false;
                }
                open.pop();
            }
            else if(c == ')'){
                if(open.top() != '('){
                    return false;
                }
                open.pop();
            }
            else if(c == ']'){
                if(open.top() != '['){
                    return false;
                }
                open.pop();
            }
            else{
                open.push(c);
            }
        }
        if(open.size() == 0){
            return true;
        }
        return false;
    }
};
