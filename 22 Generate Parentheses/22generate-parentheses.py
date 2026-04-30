class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(opn, clsd, curr):
            if len(curr) == 2*n:
                res.append(curr)
                return
            
            if opn < n:
                dfs(opn+1, clsd, curr + "(")
            
            if clsd < opn:
                dfs(opn, clsd+1, curr + ")")
        
        dfs(0, 0, "")
        return res