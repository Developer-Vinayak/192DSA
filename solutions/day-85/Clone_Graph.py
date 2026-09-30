from typing import Optional
from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            cur = queue.popleft()
            for nei in cur.neighbors:
                if nei not in clones:
                    clones[nei] = Node(nei.val)
                    queue.append(nei)
                clones[cur].neighbors.append(clones[nei])

        return clones[node]
