"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # DFS detect cycle in graph
        white, gray, black = 0, 1, 2
        tmp = head
        color = {}
        # initial all node to be white
        while tmp:
            if tmp in color:
                break
            color[tmp] = white
            tmp = tmp.next
        def dfs(head):
            # base case
            if head == None or head.next == None:
                return False
            # processing node
            color[head] = gray
            if color[head.next] == white:
                return dfs(head.next)
            elif color[head.next] == gray:
                return True
            color[head] = black # Mark node as fully processed
            return False
        return dfs(head)