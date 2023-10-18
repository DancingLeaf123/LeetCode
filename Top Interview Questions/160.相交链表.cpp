#include "leetcode_common.h"

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};
class Solution
{
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB)
    {
        unordered_set<ListNode *> visisted;
        ListNode *temp = headA;
        while (temp != nullptr)
        {
            visisted.insert(temp);
            temp = temp->next;
        }
        temp = headB;
        while (temp != nullptr)
        {
            if (visisted.count(temp))
            {
                return temp;
            }
            temp = temp->next;
        }

        return nullptr;
    }
};
