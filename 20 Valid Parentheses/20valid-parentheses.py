# What I can do here is just to remove all {}, (), [] and if the string is empty then it's a valid string
class Solution:
    def isValid(self, s: str) -> bool:
        
        while ("()" in s) or ("[]" in s) or ("{}" in s):
            s = s.replace("()","")
            s = s.replace("[]","")
            s = s.replace("{}","")
        
        if len(s) <= 0:
            return True;
        else:
            return False;
        
#     def isValid(self, s: str) -> bool:
        
#         stack = []
#         charMap = {")":"(", "}":"{", "]":"["}
        
#         for c in s:
#             if c in charMap:
#                 if stack and stack[-1] == charMap[c]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 stack.append(c)
        
#         return True if not stack else False
                
        