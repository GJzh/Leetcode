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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* node1 = head;
        ListNode* node2 = head;
        for(int i=0;i<n;i++)
        {
            if(node1->next==NULL && i<n-1)
            {
                return head;
            }
            else if(node1->next==NULL && i==n-1)
            {
                head = head->next;
                return head;
            }
            else
            {
                node1 = node1->next;
            }
        }
        node1=node1->next;
        while(node1!=NULL)
        {
            node2=node2->next;
            node1=node1->next;
        }
        node2->next=node2->next->next;
        return head;
    }
};
