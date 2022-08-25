#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <stack>
#include <limits.h> 
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

