class Solution(object):
    def isValid(self, s):
        if len(s)%2:
            return False
        stack = []
        for ch in s:
            if ch=='(':
                stack.append(')') 
            elif ch=='{':
                stack.append('}') 
            elif ch=='[':
                stack.append(']') 
            else:
                if not stack or stack.pop()!=ch:
                    return False
        return not stack   
        
