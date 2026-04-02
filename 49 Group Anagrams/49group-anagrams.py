class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ana_dic = {}

        for i in range(len(strs)):
            key_ss = "".join(sorted(strs[i]))
            if key_ss in ana_dic:
                ana_dic[key_ss].append(strs[i])
            else:
                ana_dic[key_ss] = [strs[i]]
        
        # print(ana_dic)
        return [v for v in ana_dic.values()] # list(ana_dic.values()) 