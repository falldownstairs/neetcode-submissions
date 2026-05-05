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
        if(!head){
            return nullptr;
        }
        Node* headStart = new Node(0);
        Node* res = new Node(0);
        Node* copy = new Node(head->val);
        res->next = copy;
        headStart->next = head;

        unordered_map<Node*,Node*> hashmap;

        while(head->next){
            hashmap[head] = copy;
            copy->next = new Node(head->next->val);
            copy = copy->next;
            head = head->next;
        }
        hashmap[head] = copy;
        
        copy = res->next;
        head = headStart->next;
        while(copy){
            cout<<hashmap[head]<<' '<<copy<<'\n';
            copy->random = hashmap[head->random];
            head = head->next;
            copy = copy->next;
        }

        return res->next;
    }
};
