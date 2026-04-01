class Solution:
    def isValid(self, s: str) -> bool:

        # []{}(){}[
        # [. "]"     ]
        # use this set to validate
        sset = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        # use the stack to track
        stack = []

        for i in range(len(s)):
            if s[i] in sset:
                if stack and stack[-1] == sset.get(s[i]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return False if stack else True
