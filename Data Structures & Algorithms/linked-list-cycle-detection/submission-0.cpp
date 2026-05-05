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
    bool hasCycle(ListNode* head) {
        int c = 2;
        ListNode* fastptr = head;
        while(fastptr->next && fastptr->next->next){
            fastptr = fastptr->next->next;
            head = head->next;
            if(fastptr == head){
                return true;
            }
        }
        return false;
    }
};
