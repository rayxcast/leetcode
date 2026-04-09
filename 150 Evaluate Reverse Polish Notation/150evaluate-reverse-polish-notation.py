class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        # op = {
        #     "+": 0,
        #     "-": 0,
        #     "*": 0,
        #     "/": 0
        # }
        for t in tokens:
            # if t not in op:
            #     stack.append(t)
            #     continue
            # print(f"perform {t} operation:", stack)
            # b = int(stack.pop())
            # a = int(stack.pop())
            # print(f"{a} {t} {b}")
            if t == "+": # add two last items in stack
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(a+b) 
            elif t == "-": # substract two last items in stack
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(a-b)
            elif t == "*": # multiple last two values in stack
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(a*b)
            elif t == "/": # divide last two values in stack
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(math.trunc(a/b))
            else:
                stack.append(t)
        # print(stack)

        return stack[0]