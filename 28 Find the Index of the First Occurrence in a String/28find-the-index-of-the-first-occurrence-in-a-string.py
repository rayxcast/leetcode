class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)

        for i, a in enumerate(haystack):
            if a == needle[0] and haystack[i:i+l] == needle:
                return i
        
        return -1