#include<iostream>
#include <stack>
#include <string>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        if(l1 == NULL)  return l2;
        if(l2 == NULL)  return l1;
        ListNode *head;
        if(l1->val >= l2->val){
            head = l2;
            l2 = l2->next;
        }
        else{
            head = l1;
            l1 = l1->next;
        }
        ListNode *p = head;
        while(l1 && l2){
            if(l1->val <= l2->val){
                p->next = l1;p = l1;l1 = l1->next;
            }
            else{
                p->next = l2;p = l2;l2 = l2->next;
            }
        }
        if(l1 == NULL)  p->next = l2;
        else    p->next = l1;
        return head;
    }
};