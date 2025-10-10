class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(strs)
        if l == 0:
            return ""

        # find the smallest word in the array by lenght
        sw = strs[0]
        currSW = len(strs[0])
        for i in range(1, l):
            if len(strs[i]) < currSW:
                sw = strs[i]
                currSW = len(strs[i])

        lcp = sw
        # print("First lcp:", lcp)
        while len(lcp) > 0:
            found = True
            for s in strs:
                sPrefix = s[:len(lcp)]
                # print("Checking lcp with sPrefix =", sPrefix)
                if lcp != sPrefix:
                    found = False
                    lcp = lcp[:len(lcp)-1]
                    # print("New lcp:", lcp)
                    break
            if found == True:
                return lcp
        
        return ""      