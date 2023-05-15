class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        # We can obtain the answer by checking if both strings are the same lenght, have the same characters, and each have the same number of distinct characters. Ex: aaabbc, abbccc: 3 chars + 2 chars + 1 char

        # First let's check the lenght
        if len(word1) != len(word2):
            return False
        
        # Now let's check if have the same characters
        word1_set, word2_set = set(word1), set(word2)

        if word1_set != word2_set:
            return False

        w1, w2 = {}, {}
        # Now let's check if each have the same number of distinct characters
        for c in word1:
            w1[c] = w1.get(c, 0) + 1

        for c in word2:
            w2[c] = w2.get(c, 0) + 1

        if sorted(list(w1.values())) != sorted(list(w2.values())):
            return False

        return True
        
