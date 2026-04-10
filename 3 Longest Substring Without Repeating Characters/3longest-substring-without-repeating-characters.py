class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = 0
        curr_sub = set()
        max_sub = 0

        for r in range(len(s)):
            while s[r] in curr_sub:
                curr_sub.remove(s[l])
                l+=1
            curr_sub.add(s[r])
            max_sub = max(max_sub, r-l+1)
            r+=1
        
        # print(curr_sub)

        return max_sub