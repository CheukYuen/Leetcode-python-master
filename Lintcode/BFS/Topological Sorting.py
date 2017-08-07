# Definition for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
import collections


class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of graph nodes in topological order.
    """

    def topSort(self, graph):
        # write your code here
        result = []
        hashmap = {}
        for node in graph:
            for nei in node.neighbors:
                if nei in hashmap:
                    hashmap[nei] += 1
                else:
                    hashmap[nei] = 1

        queue = collections.deque()

        for node in graph:
            if node not in hashmap:
                queue.append(node)
                result.append(node)

        while queue:
            node = queue.popleft()
            for nei in node.neighbors:
                hashmap[nei] = hashmap[nei] - 1

                if hashmap[nei] == 0:
                    result.append(nei)
                    queue.append(nei)
        return result


test = Solution()
print test.topSort()


