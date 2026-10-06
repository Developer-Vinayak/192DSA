from collections import defaultdict, deque
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(set)
        indegree = {c: 0 for w in words for c in w}
        for w1, w2 in zip(words, words[1:]):
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for a, b in zip(w1, w2):
                if a != b:
                    if b not in adj[a]:
                        adj[a].add(b)
                        indegree[b] += 1
                    break  
        queue = deque(c for c in indegree if indegree[c] == 0)
        result = []
        while queue:
            c = queue.popleft()
            result.append(c)
            for nxt in adj[c]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return "".join(result) if len(result) == len(indegree) else ""
