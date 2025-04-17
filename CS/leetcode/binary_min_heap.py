"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
"""

# min-binary-heap
class MinStack(object):

    def __init__(self):
        self.min_binary_heap = []
        self.length = len(self.min_binary_heap)

    # parent node
    def parent(self, i):
        return (i - 1) // 2 if i > 0 else i

    # left child node
    def left(self, i):
        l = 2*i + 1
        return l if l < self.length else i

    def right(self, i):
        r = 2*i + 2
        return r if r < self.length else i

    def min_heapify_up(self, i):
        p = self.parent(i)
        if p == i: return
        if self.min_binary_heap[i] < self.min_binary_heap[p]:
            self.min_binary_heap[i], self.min_binary_heap[p] = self.min_binary_heap[p], self.min_binary_heap[i]
            self.min_heapify_up(p)

    def min_heapify_down(self, i):
        l,r = self.left(i), self.right(i)
        c = l if self.min_binary_heap[l] < self.min_binary_heap[r] else r
        if c == i: return
        if self.min_binary_heap[i] > self.min_binary_heap[c]:
            self.min_binary_heap[i], self.min_binary_heap[c] = self.min_binary_heap[c], self.min_binary_heap[i]
            self.min_heapify_down(c)


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.min_binary_heap.append(val)
        self.length += 1
        i = len(self.min_binary_heap) - 1
        self.min_heapify_up(i)


    def deletMin(self):
        """
        :rtype: None
        """
        self.min_binary_heap[0],self.min_binary_heap[-1] = self.min_binary_heap[-1], self.min_binary_heap[0]
        self.min_binary_heap.pop()
        self.length -= 1
        self.min_heapify_down(0)

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_binary_heap[0]