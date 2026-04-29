class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        s = []

        def dfs(i, d):
            # print(d, i)
            if i == len(nums):
                # print("adding to res:", s)
                res.append(s.copy())
                return
            
            s.append(nums[i])
            dfs(i+1, "left")

            s.pop()
            dfs(i+1, "right")

        dfs(0, "start")
        return res