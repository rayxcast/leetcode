class Solution:
    def reverseWords(self, s: str) -> str:

        l = len(s)
        reverse = []
        w = ""
        for i in range(l):
            if s[i] != " ":
                w += s[i]
            else:
                if w != "":
                    reverse.append(w)
                w = ""

        if w != "":
            reverse.append(w)
        
        print(reverse)
        output = ""
        l = len(reverse)-1
        for i in range(l, -1, -1):
            output += reverse[i] 
            if i != 0:
                output += " "
        
        return output

