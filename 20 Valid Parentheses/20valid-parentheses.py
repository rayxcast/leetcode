class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
             
        close = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        stack = []
        for c in s:
            if c in close and stack:
                # print(c, stack[-1], close[c])
                if stack[-1] == close[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        # print(stack)

        return True if len(stack) == 0 else False
            