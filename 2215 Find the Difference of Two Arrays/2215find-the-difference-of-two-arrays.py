class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # a0 = []
        # for i in nums1:
        #     if i not in nums2 and i not in a0:
        #         a0.append(i)
        
        # a1 = []
        # for i in nums2:
        #     if i not in nums1 and i not in a1:
        #         a1.append(i)
        
        # return [a0, a1]

        # Let's use sets which makes looking for an element constanct and doesn't contain duplicates
        nums1_set, nums2_set = set(nums1), set(nums2)
        a0, a1 = set(), set()
        for i in nums1:
            if i not in nums2_set:
                a0.add(i)
        
        for i in nums2:
            if i not in nums1_set:
                a1.add(i)
        
        return [list(a0), list(a1)]

            