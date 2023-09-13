class Solution:
    def reverseVowels(self, s: str) -> str:

        # using a stack
        # vowels = ('a', 'e', 'i', 'o', 'u')
        # stack = []
        # for c in s:
        #     if c.lower() in vowels:
        #         stack.append(c)

        # newS = ""
        # for i in range(len(s)):
        #     if s[i].lower() in vowels:
        #         newS += stack.pop()
        #     else:
        #         newS += s[i]
        
        # return newS

        # using two pointers
        l = 0
        r = len(s)-1
        # newS = ""
        vowels = ('a', 'e', 'i', 'o', 'u')
        arrS = []
        for c in s:
            arrS.append(c)

        while(l < r):
            if s[l].lower() in vowels and s[r].lower() in vowels:
                # newS += s[r]
                temp = arrS[l]
                arrS[l] = arrS[r]
                arrS[r] = temp
                l += 1
                r -= 1
            
            if s[l].lower() not in vowels:
                # newS += s[l]
                l += 1

            if s[r].lower() not in vowels:
                r -= 1
        
        # print(arrS)
        return "".join(arrS)
            


        