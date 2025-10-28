class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if str1.replace(str2, "") == "":
            return str2
        if str2.replace(str1, "") == "":
            return str1
        
        # get smallest string
        smallest = str2
        largest = str1
        if len(str1) < len(str2):
            smallest = str1
            largest = str2
        
        if smallest not in largest:
            return ""

        # print("Runing algo...")
        gcds = ""
        curr = ""
        for c in largest:
            curr+=c
            if len(curr) > len(gcds) and len(largest)%len(curr) == 0 and len(smallest)%len(curr) == 0:
                gcds=curr
            if len(curr) > len(smallest):
                break
        # print("last curr:", curr)
        # print("gcds:", gcds)
        if largest.replace(gcds, "") == "" and smallest.replace(gcds, "") == "":
            return gcds

        return ""