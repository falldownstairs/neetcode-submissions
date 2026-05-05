/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* res;
        ListNode* p1;
        ListNode* p2;
        res = p1 = p2 = new ListNode(-1, head);

        int c = n+1;

        while(c>0){
            c--;
            p2 = p2->next;
        }
        // cout << p2->val <<' ';
        while(p2){
            p2 = p2->next;
            p1 = p1->next;
        }
        cout << p1->val;
        p1->next = p1->next->next;
        

        
        return res->next;
    }
};
