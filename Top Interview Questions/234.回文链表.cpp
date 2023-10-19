#include "leetcode_common.h"

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    bool isPalindrome(ListNode *head)
    {
        vector<int> list;
        while (head)    
        {
            list.emplace_back(head->val);
            head = head->next;
        }
        int n = list.size();
        for (int i = n - 1; i >= 0; i--)
        {
            if (list[i] != list[n - i - 1])
            {
                return false;
            }
        }
        return true;
    }
};