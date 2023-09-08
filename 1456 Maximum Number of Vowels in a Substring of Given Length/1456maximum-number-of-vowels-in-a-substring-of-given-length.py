class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowelsSet = ("a", "e", "i", "o", "u")
        maxVowels = 0
        currVowels = 0
        for i in range(len(s)):
            if s[i] in vowelsSet:
                currVowels += 1
            
            if i == k-1: # first substring of size k is found
                maxVowels = currVowels
            elif i > k-1:
                if s[i-k] in vowelsSet:
                    currVowels -= 1
                if currVowels > maxVowels:
                    maxVowels = currVowels
            
        return maxVowels
        