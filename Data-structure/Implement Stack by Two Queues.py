import collections


class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()

    def swapQueue(self):
        temp = self.queue1
        self.queue1 = self.queue2
        self.queue2 = temp

    def move(self):
        size = len(self.queue1)
        for i in range(size - 1):
            self.queue2.append(self.queue1.popleft())

    # @param x, an integer, push a new item into the stack
    # @return nothing
    def push(self, x):
        # Write your code here
        self.queue1.append(x)

    # @return nothing, pop the top of the stack
    def pop(self):
        # Write your code here
        if not self.isEmpty():
            self.move()
            self.queue1.popleft()
            self.swapQueue()

    # @return an integer, return the top of the stack
    def top(self):
        # Write your code here
        if not self.isEmpty():
            self.move()
            item = self.queue1.popleft()
            self.swapQueue()
            self.queue1.append(item)
            return item

    # @return an boolean, check the stack is empty or not.
    def isEmpty(self):
        # Write your code here
        return not len(self.queue1)