class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first let's check a basic invalidation
        if len(s) != len(t):
            return False

        ana_s_dic = {}
        ana_t_dic = {}

        for c in s:
            if c in ana_s_dic:
                ana_s_dic[c] += 1
            else: 
                ana_s_dic[c] = 1

        for c in t:
            if c in ana_t_dic:
                ana_t_dic[c] += 1
            else: 
                ana_t_dic[c] = 1
        
        if ana_s_dic == ana_t_dic:
            return True
        
        return False