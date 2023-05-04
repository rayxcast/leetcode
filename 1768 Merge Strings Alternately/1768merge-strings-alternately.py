class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        l = 0
        longer_word = ""
        if len(word1) == len(word2):
            l = len(word1)
        elif len(word1) > len(word2):
            l = len(word2)
            longer_word = word1
        else:
            l = len(word1)
            longer_word = word2

        merge = ""
        i = 0
        while i < l:
            merge += word1[i]
            merge += word2[i]
            i+=1
        
        if longer_word != "": # if there is a word longer than the other
            merge += longer_word[i:]


        return merge
