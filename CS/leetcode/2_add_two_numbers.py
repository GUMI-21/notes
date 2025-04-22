# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        new_node = ListNode()
        head = new_node
        check = 0
        # process l1.length = l2.length
        while l1 is not None and l2 is not None:
            new_node.val = l1.val + l2.val + check
            check = 0
            # 进位
            if new_node.val >= 10:
                check = new_node.val / 10
                new_node.val = new_node.val % 10
            l1 = l1.next
            l2 = l2.next
            new_node.next = ListNode()
            new_node = new_node.next

        if l1 is not None:
            while l1 is not None:
                new_node.val = l1.val + check
                # reset check
                check = 0
                if new_node.val >= 10:
                    check = new_node.val / 10
                    new_node.val = new_node.val % 10
                l1 = l1.next
                new_node.next = ListNode()
                new_node = new_node.next

        if l2 is not None:
            while l2 is not None:
                new_node.val = l2.val + check
                # reset check
                check = 0
                if new_node.val >= 10:
                    check = new_node.val / 10
                    new_node.val = new_node.val % 10
                l2 = l2.next
                new_node.next = ListNode()
                new_node = new_node.next
        # because every step we add a new_node to tail, so need to delete the tail
        tmp = head.next
        prev = head
        while tmp is not None:
            if tmp.next is None:
                prev.next = None
                break
            tmp = tmp.next
            prev = prev.next
        # if check > 0, means After the addition process, a carry of 1 is required.
        if check > 0:
            prev.next = ListNode()
            prev = prev.next
            prev.val = check

        return head
