class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Create a map which keys represent the characters as ID of each string in the array
        anaMap = {}
        def getStringId(s):
            count = [0]*26
            for c in s:
                count[ord(c) - ord("a")] += 1
            return tuple(count)

        for s in strs:
            sId = getStringId(s)
            if sId not in anaMap:
                anaMap[sId] = []
            anaMap[sId].append(s)
        
        return [anaMap[key] for key in anaMap]
