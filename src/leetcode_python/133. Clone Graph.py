# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/description/

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        
        def clone(node):
            if node in visited:
                return visited[node]
            
            new = Node(node.val)
            visited[node] = new
            
            for n in node.neighbors:
                new.neighbors.append(clone(n))
            return new
                
        return clone(node) if node else None
