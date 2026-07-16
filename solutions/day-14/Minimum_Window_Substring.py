from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        a = {}
        extra = {}
        target = {}
        res = ""
        for i in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
            a[i] = 0
            extra[i] = 0
            target[i] = 0
        for i in t:
            target[i] += 1
        j = 0
        for i in range(len(s)):
            ch = s[i]
            if a[ch] < target[ch]:
                a[ch] += 1
            else:
                extra[ch] += 1
            if i >= len(t) - 1:
                while True:
                    prev = 0
                    if extra[s[j]] == 0:
                        a[s[j]] -= 1
                        prev = 1
                    else:
                        extra[s[j]] -= 1
                    j += 1
                    if a != target:
                        j -= 1
                        if prev == 1:
                            a[s[j]] += 1
                        else:
                            extra[s[j]] += 1
                        break
                if a == target:
                    value = s[j:i + 1]
                    res = value if res == "" or len(value) < len(res) else res
        return res
