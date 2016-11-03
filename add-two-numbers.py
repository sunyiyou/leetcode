
class Solution(object):
    def addTwoNumbers_my(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1 = l1
        cur2 = l2
        c = 0
        while cur1.next and cur2.next:
            a = cur1.val
            b = cur2.val
            cur1.val = (a+b+c) % 10
            c = (a+b+c) // 10
            cur1 = cur1.next
            cur2 = cur2.next
        
        a = cur1.val
        b = cur2.val
        cur1.val = (a+b+c) % 10
        c = (a+b+c) // 10
        
        if cur2.next:        
            cur1.next = cur2.next
            cur1 = cur1.next
        elif cur1.next:
            cur1 = cur1.next
        else:
            if c == 1:
                cur1.next = ListNode(1)
            return l1
            
        while cur1.next:
            if c == 1:
                if cur1.val == 9:
                    cur1.val = 0
                    c = 1
                else:
                    cur1.val += 1
                    c = 0
            cur1 = cur1.next
        if c == 1:
            if cur1.val == 9:
                cur1.val = 0
                cur1.next = ListNode(1)
            else:
                cur1.val += 1
        return l1
                
                
    def addTwoNumbers(self, l1, l2):

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        current, carry = dummy, 0

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = val / 10, val % 10
            current.next = ListNode(val)
            current = current.next

        if carry == 1:
            current.next = ListNode(1)

        return dummy.next