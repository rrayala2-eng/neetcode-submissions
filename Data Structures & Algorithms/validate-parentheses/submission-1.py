class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeto = {')' : '(',']':'[', '}':'{'}

        for c in s:
            if c in closeto:
                if stack and stack[-1] == closeto[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        