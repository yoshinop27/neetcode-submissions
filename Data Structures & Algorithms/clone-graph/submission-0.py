"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        ret = {} 
        seen = set()
        qu = deque()
        qu.append(node)

        if not node:
            return None

        while qu:
            node = qu.popleft()
            neighbors = []
            # Exit if we have already evaluated
            if node in seen:
                continue
            
            seen.add(node)
            for neighbor in node.neighbors:
                neighbors.append(neighbor.val)
                qu.append(neighbor)
            ret[node.val] = neighbors
        
        root = None
        ## Create Nodes
        nodes = [None] * (len(ret)+1)
        for key, value in ret.items():
            nw = Node(key,[])
            nodes[key] = nw
        
        ## Build map
        for key, value in ret.items():
            node = nodes[key]
            for val in value:
                node.neighbors.append(nodes[val])
        return nodes[1]
        
            
            
