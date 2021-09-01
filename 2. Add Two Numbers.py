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
                
        while l1 or l2 or carry:            
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2 + carry, 10)    
                      
            result_tail.next = ListNode(out)
            result_tail = result_tail.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
               
        return result.next



('r', ListNode{val: 0, next: None}, 139952232452624)
('r_t', ListNode{val: 0, next: None}, 139952232452624)
('r_n', None, 93844689430896)
('r_t_n', None, 93844689430896)
('carry', None, 93844689430896)

result_tail.next = ListNode(1)
('r', ListNode{val: 0, next: ListNode{val: 1, next: None}}, 139952232452624)
('r_t', ListNode{val: 0, next: ListNode{val: 1, next: None}}, 139952232452624)
('r_n', ListNode{val: 1, next: None}, 139952232452688)
('r_t_n', ListNode{val: 1, next: None}, 139952232452688)
('r_n_n', None, 93844689430896)
('r_t_n_n', None, 93844689430896)
('carry', None, 93844689430896)

result_tail = result_tail.next
('r', ListNode{val: 0, next: ListNode{val: 1, next: None}}, 139952232452624)
('r_t', ListNode{val: 1, next: None}, 139952232452688)
('r_n', ListNode{val: 1, next: None}, 139952232452688)
('r_t_n', None, 93844689430896)

