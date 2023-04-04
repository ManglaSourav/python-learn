

"""

# Definition for a Node.
"""

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def buildGraph() -> Node:
    """
    Given Graph:
    1--2
    |  |
    4--3
    """
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node3, node1]
    return node1


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            copy  = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
                 
            return copy 
        return dfs(node) if node else None

print(Solution().cloneGraph(buildGraph()).neighbors[0].val)