class LinkedNode:
    def __init__(self, key=None, val=None, next=None):
        self.key = key
        self.val = val
        self.next = next


class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        # write your code here
        self.hash = {}
        self.head = LinkedNode()
        self.tail = self.head
        self.capacity = capacity

    # when set and get
    def push_back(self, node):
        self.hash[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    # when cache is full.
    def pop_front(self):
        del self.hash[self.head.next.key]
        self.head.next = self.head.next.next
        self.hash[self.head.next.key] = self.head

    # handle node in mid
    def move_to_tail(self, prev):
        node = prev.next
        if node is self.tail:
            return
        prev.next = node.next
        if node.next:
            self.hash[node.next.key] = prev
            node.next = None
        self.push_back(node)

        # @return an integer

    def get(self, key):
        # write your code here
        if key not in self.hash:
            return -1
        self.move_to_tail(self.hash[key])
        return self.hash[key].next.val
        # node = self.hash[key]
        # self.move_to_tail(node)
        # return node.next.val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # write your code here
        if key in self.hash:
            self.move_to_tail(self.hash[key])
            self.hash[key].next.val = value
        else:
            self.push_back(LinkedNode(key, value))
            if len(self.hash) > self.capacity:
                self.pop_front()


obj = LRUCache(3)
obj.set(1, 1)
obj.set(2, 2)
obj.set(3, 3)
obj.set(4, 4)
print obj.get(4)
print obj.get(3)
print obj.get(2)
print obj.get(1)