# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0
        print("result", result)
        print("result.next", result.next)
                
        while l1 or l2 or carry:            
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2 + carry, 10)    
                      
            result_tail.next = ListNode(out)
            result_tail = result_tail.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)

        return result.next


an = Solution()
an.addTwoNumbers(l1,l2)

('count', 0)
('b result_tail in while', ListNode{val: 0, next: None})
('b result in while', ListNode{val: 0, next: None})
('m result_tail in while', ListNode{val: 0, next: ListNode{val: 7, next: None}})
('m result in while', ListNode{val: 0, next: ListNode{val: 7, next: None}})
('result_tail in while', ListNode{val: 7, next: None})
('result in while', ListNode{val: 0, next: ListNode{val: 7, next: None}})

('count', 1)
('b result_tail in while', ListNode{val: 7, next: None})
('b result in while', ListNode{val: 0, next: ListNode{val: 7, next: None}})
('m result_tail in while', ListNode{val: 7, next: ListNode{val: 0, next: None}})
('m result in while', ListNode{val: 0, next: ListNode{val: 7, next: ListNode{val: 0, next: None}}})
('result_tail in while', ListNode{val: 0, next: None})
('result in while', ListNode{val: 0, next: ListNode{val: 7, next: ListNode{val: 0, next: None}}})

('count', 2)
('b result_tail in while', ListNode{val: 0, next: None})
('b result in while', ListNode{val: 0, next: ListNode{val: 7, next: ListNode{val: 0, next: None}}})
('m result_tail in while', ListNode{val: 0, next: ListNode{val: 8, next: None}})
('m result in while', ListNode{val: 0, next: ListNode{val: 7, next: ListNode{val: 0, next: ListNode{val: 8, next: None}}}})
('result_tail in while', ListNode{val: 8, next: None})
('result in while', ListNode{val: 0, next: ListNode{val: 7, next: ListNode{val: 0, next: ListNode{val: 8, next: None}}}})
