/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode* result;
        ListNode* temp;
        result->next=head;
        for(ListNode* it=result;it->next!=NULL;it=it->next->next)
        {
            if(it->next->next==NULL)
            {
                return result->next;
            }
            else
            {
                temp=it->next;
                it->next=temp->next;
                temp->next=it->next->next;
                it->next->next=temp;
            }
        }
        return result->next;
    }
};
