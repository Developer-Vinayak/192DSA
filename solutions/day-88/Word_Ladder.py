from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])
        visited = {beginWord}
        letters = 'abcdefghijklmnopqrstuvwxyz'

        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for ch in letters:
                    if ch == word[i]:
                        continue
                    nxt = word[:i] + ch + word[i + 1:]
                    if nxt in words and nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, steps + 1))

        return 0
