class LinkedNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        # write your code here
        self.capacity = capacity
        self.head = LinkedNode()
        self.tail = self.head
        self.hash = {}

    def push_back(self, node):
        self.hash[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    def pop_front(self):
        del self.hash[self.head.next.key]
        self.head.next = self.head.next.next
        self.hash[self.head.next.key] = self.head

    # head-> ...node ->... -> tail
    # head-> ...->tail -> node
    def kick(self, prev):
        curt = prev.next
        if curt is self.tail:
            return
        prev.next = prev.next.next
        self.hash[prev.next.key] = prev
        curt.next = None
        self.push_back(curt)

    # @return an integer
    def get(self, key):
        # write your code here
        if key not in self.hash:
            return -1
        self.kick(self.hash[key])
        return self.hash[key].next.value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        # write your code here
        if key in self.hash:
            self.hash[key].next.value = value
            self.kick(self.hash[key])
        else:
            self.push_back(LinkedNode(key, value))
            if len(self.hash) > self.capacity:
                self.pop_front()


t = LRUCache(3)
t.set(11, 'a')
t.set(22, 'b')
t.set(33, 'c')
t.set(44, 'd')

print t.get(11)
print t.get(33)

