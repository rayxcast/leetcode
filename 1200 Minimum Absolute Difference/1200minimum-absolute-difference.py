class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # sort the array
        sArr = sorted(arr)

        # use Left and right pointers to traverse the array
        left = 1
        right = 2

        # track MAD
        currMAD = sArr[1] - sArr[0]

        MAD_DIC = defaultdict(list)
        MAD_DIC[currMAD].append([sArr[0], sArr[1]])

        # first find the Minimum Absolute Difference (MAD)
        while right < len(sArr):
            MAD = sArr[right] - sArr[left]
            MAD_DIC[MAD].append([sArr[left], sArr[right]])
            if MAD < currMAD:
                currMAD = MAD
            left+=1
            right+=1
        
        
        return MAD_DIC[currMAD]
            