"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """

        # recursive solution
        def isSame(node1, node2):
            if node1 is None:
                if node2 is None:
                    return True
                else:
                    return False
            if node2 is None:
                if node1 is None:
                    return True
                else:
                    return False
            if node1.val != node2.val:
                return False
            else:
                return isSame(node1.left, node2.left) and isSame(node1.right, node2.right)
        return isSame(p, q)

# test case
if __name__ == "__main__":
    print(111111)
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    print(Solution().isSameTree(p, q)) 
    # more test case
    p = TreeNode(1, TreeNode(2))
    q = TreeNode(1, None, TreeNode(2))
    print(Solution().isSameTree(p, q)) 
    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(1), TreeNode(2))
    print(Solution().isSameTree(p, q)) 