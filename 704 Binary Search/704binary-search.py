class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums)-1
        mid = (l+r)//2

        while l <= r:
            # print("curr mid index:", mid)
            if target > nums[mid]:
                # print(target, "larger than", nums[mid])
                l = mid+1
                mid = (l+r)//2
            elif target < nums[mid]:
                # print(target, "smaller than", nums[mid])
                r = mid-1
                mid = (l+r)//2
            else:
                # print("found:", nums[mid])
                return mid

        return -1