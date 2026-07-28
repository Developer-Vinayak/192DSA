class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        n = len(min(strs, key=len))
        prefix = ""
        for i in range(n):
            ch = strs[0][i]
            if all(s[i] == ch for s in strs):
                prefix += ch
            else:
                break
        return prefix
