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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode* res = new ListNode(0);
        ListNode* curr = res;
        int smallest = 1001;
        int smallestindex;
        while(lists.size()>0){
            for(int i = 0;i<lists.size();i++){
                if(lists[i]->val<smallest){
                    smallest = lists[i]->val;
                    smallestindex = i;
                }
            }
            curr->next = new ListNode(lists[smallestindex]->val);
            curr = curr->next;
            lists[smallestindex] = lists[smallestindex]->next;
            if(!lists[smallestindex]){
                lists.erase(lists.begin()+smallestindex);
            }
            smallest = 1001;
        }
        return res->next;
    }
};
