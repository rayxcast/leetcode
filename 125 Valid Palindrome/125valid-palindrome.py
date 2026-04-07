class Solution:
    def isPalindrome(self, s: str) -> bool:
        def format_string(s):
            return "".join(filter(str.isalnum, s)).lower()
        
        s = format_string(s)
        print(s)
        if s == "":
            return True
        
        l = 0
        r = len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False
            l+=1
            r-=1
        
        return True