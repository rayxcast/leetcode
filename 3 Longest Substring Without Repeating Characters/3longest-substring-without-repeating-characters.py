# Let's have a function which iterate through the strign and save the substring until a
# repeating character is found. The current substring will be saved in a variable "longestSub"
# and another variable "currentSub" will be used to form a new substring when a repeated char is found
# if len(currentSub) > len(longestSub): longestSub = currentSub

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSub = ""
        currentSub = ""
        i = 0
        c = 0
        while i < len(s):
            if s[i] not in currentSub:
                currentSub += s[i]
            else:
                c+=1
                i = c
                currentSub = s[c] # reset the current substring
            
            if len(currentSub) > len(longestSub):
                longestSub = currentSub
            
            i += 1

        return len(longestSub)