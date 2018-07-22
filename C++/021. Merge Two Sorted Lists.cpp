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
	ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
		ListNode result(-1);
		for (ListNode* it = &result; l1 != NULL || l2 != NULL; it = it->next) {
		    if (l1 == NULL)
		    {
		        it->next = l2;
		        break;
		    }
		    if (l2 == NULL)
		    {
		        it->next = l1;
		        break;
		    }
			if (l1->val <= l2->val) {
				it->next = l1;
				l1 = l1->next;
			}
			else {
				it->next = l2;
				l2 = l2->next;
			}
		}
		return result.next;
	}
};
