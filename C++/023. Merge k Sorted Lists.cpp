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
    ListNode* mergeTwo(ListNode* list1, ListNode* list2)
    {
        if (list1 == NULL) return list2;
        if (list2 == NULL) return list1;
        ListNode* head = new ListNode(-1);
        head->next = list1;
        ListNode* prev = head, *left = list1, *right = list2;
        while(left != NULL && right != NULL)
        {
            if (right->val < left->val)
            {
                ListNode* temp = right->next;
                prev->next = right;
                prev->next->next = left;
                prev = right;
                right = temp;
            }
            else
            {
                prev = left;
                left = left->next;
            }
        }
        
        if (right != NULL)
        {
            prev->next = right;
        }
        
        return head->next;
    }
        
    ListNode* mergeKLists(vector<ListNode*>& lists) 
    {
        if (lists.size() == 0) return NULL; 
        while(lists.size() > 1)
        {
            int end = lists.size() / 2 - 1;
            for (int left = 0, right = lists.size() - 1 ; left <= end; left++, right--)
            {
                lists[left] = mergeTwo(lists[left], lists[right]);
                lists.pop_back();
            }
        }
        return lists[0];
    }
};
