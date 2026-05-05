/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        unordered_map<Node*,Node*> toCopy;
        
        Node* cur = head;
        while(cur){
            Node* copy = new Node(cur->val);
            toCopy[cur] = copy;
            cur=cur->next;
        }

        cur = head;

        while(cur){
            toCopy[cur]->next = toCopy[cur->next];
            toCopy[cur]->random = toCopy[cur->random];
            cur=cur->next;
        }
        return toCopy[head];

    }
};
