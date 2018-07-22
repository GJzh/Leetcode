class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* result;
        result = new ListNode(-1);
        int val=0;
        if(l1==NULL && l2==NULL)
        {
            return NULL;
        }
        else if(l1==NULL)
        {
            return l2;
        }
        else if(l2==NULL)
        {
            return l1;
        }
        else
        {
            result->next=l1;
            val = l1->val + l2->val;
            l1->val = val%10;
            if(val>=10)
            {
                if(l1->next==NULL)
                {
                    l1->next = new ListNode(1);
                }
                else if(l2->next==NULL)
                {
                    l2->next = new ListNode(1);
                }
                else
                {
                    l1->next->val = l1->next->val+1;
                }
            }
            result->next->next=addTwoNumbers(l1->next, l2->next);
        }
        return result->next;
    }
};
