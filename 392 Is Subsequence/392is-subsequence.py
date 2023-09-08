class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0
        if s == "":
            return True

        for c in t:
            if s[si] == c:
                si += 1
            if si >= len(s): # if si is out of bounce from s then all its chars are in t
                return True

        # if all chars in s are not in t then it means there is not a subsequence or not all chars in s are in t in the same order
        return False
            