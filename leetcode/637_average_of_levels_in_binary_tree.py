"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.
Answers within 10-5 of the actual answer will be accepted.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        # BFS
        parent = {}
        def init_parent(node):
            if node is None:
                return
            if node not in parent:
                parent[node] = None
                init_parent(node.left)
                init_parent(node.right)
        init_parent(root)
        parent[root] = root
        level = [[root]]
        # bfs form levels
        while 0 < len(level[-1]):
            level.append([])
            for node in level[-2]:
                if node.left:
                    if parent[node.left] is None:
                        parent[node.left] = node
                        level[-1].append(node.left)
                if node.right:
                    if parent[node.right] is None:
                        parent[node.right] = node
                        level[-1].append(node.right)
        # find average from every level
        rlist = []
        for nums in level:
            if len(nums) == 0:
                continue
            a = 0
            count = 0
            for i in nums:
                a += i.val
                count += 1
            rlist.append(float(a)/float(count))
        return rlist

# a better answer
class Solution:
    def averageOfLevels(self, root: TreeNode) -> array[float]:
        q, ans = [root], []
        while len(q):
            qlen, row = len(q), 0
            for i in range(qlen):
                curr = q.pop(0)
                row += curr.val
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            ans.append(row/qlen)
        return ans