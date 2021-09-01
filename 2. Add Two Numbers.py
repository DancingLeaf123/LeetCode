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



('r', ListNode{val: 0, next: None}, 140331611189776)
('r_t', ListNode{val: 0, next: None}, 140331611189776)
('r_n', None, 94764619159920)
('r_t_n', None, 94764619159920)
('==', True, 94764619161104, <type 'bool'>)
('buer', True, 94764619161104, <type 'bool'>)
('is', True, 94764619161104)

('r', ListNode{val: 0, next: ListNode{val: 1, next: None}}, 140331611189776)
('r_t', ListNode{val: 0, next: ListNode{val: 1, next: None}}, 140331611189776)
('r_n', ListNode{val: 1, next: None}, 140331611189840)
('r_t_n', ListNode{val: 1, next: None}, 140331611189840)
('r_n_n', None, 94764619159920)
('r_t_n_n', None, 94764619159920)
('==', True, 94764619161104)
('is', True, 94764619161104)

('r', ListNode{val: 0, next: ListNode{val: 1, next: None}}, 140331611189776)
('r_t', ListNode{val: 1, next: None}, 140331611189840)
('r_n', ListNode{val: 1, next: None}, 140331611189840)
('r_t_n', None, 94764619159920)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

"""        
 output is also a listNode object.  so how to?
 l1 = [2,4,3]
 l2 = [5,6,4]
 output should be [7,0,8]

the only math is carry 1 to the next node, so
"""
# output = ListNode(0)
# move_point = output

carry = 0
while (l1 or l2 or carry):
    num = 0
    add_result = l1.val + l2.val + carry
    if add_result lt 9:
        add_result = add_result
        carry = 0
    else:
        add_result = 0
        carry = 1

    if num lt 1:
        output = ListNode(add_result)
        move_point = output
        num += 1

    if num gt 0:
        move_point.next = ListNode(add_result)
        move_point = move_point.next

    
    l1 = l1.next
    l2 = l2.next


return  output


# if have a carry it should be add in the next version. and there still have None situtation,



