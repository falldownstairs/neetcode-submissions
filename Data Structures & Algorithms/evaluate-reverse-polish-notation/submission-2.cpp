class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        for(string val : tokens){
            if(val == "+"){
                int a = s.top();
                s.pop();
                int b = s.top();
                s.pop();
                s.push(a + b);
            }
            else if(val == "-"){
                int a = s.top();
                s.pop();
                int b = s.top();
                s.pop();
                s.push(b - a);
            }
            else if(val == "*"){
                int a = s.top();
                s.pop();
                int b = s.top();
                s.pop();
                s.push(a * b);
            }
            else if(val == "/"){
                int a = s.top();
                s.pop();
                int b = s.top();
                s.pop();
                s.push(b / a);
            }
            else{
                s.push(stoi(val));
            }
        }
        return s.top();
        
    }
};
