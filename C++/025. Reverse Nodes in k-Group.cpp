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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(head==NULL || k<=1){return head;}
        ListNode* dummy = new ListNode(0);
        dummy->next=head;
        ListNode* prev=dummy, *next, *node=head, *start, *end, *temp;
        while(node)
        {
            for (int i=0;i<k;i++)
            {
                if (node==NULL){return dummy->next;}
                end = node;
                node=node->next;
            }
            next=node;
            start = prev->next;
            node=start;
            for (int i=0;i<k-1;i++)
            {
                temp=node;
                prev->next = prev->next->next;
                node = prev->next;
                temp->next=end->next;
                end->next=temp;
            }
            node = next;
            prev = start;
        }
        return dummy->next;
    }
};
