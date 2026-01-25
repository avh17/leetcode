class Solution(object):
    def isValid(self, s):
        hash_map = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        stack = []
        for c in s:
            if c in hash_map:
                if stack and stack[-1]==hash_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False