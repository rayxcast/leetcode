class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Sort the array
        # candies.sort() # time complexity: O(nlog(n))

        # since we have the array sorted then we can check if for each i kid candies + the extraCandies is greater than the last kid in the array which is the one who has the most canides

        # for i in range(len(candies)):
        #     if candies[i] + extraCandies >= candies[len(candies)-1]:
        #         result[i] = True
        #     else:
        #         result[i] = False
        
        # return result

        # since the order matters then we need to find the kid with the most candies
        greatersCandyHolderAmount = 0
        for i in range(len(candies)): # time complexity = O(n)
            if candies[i] > greatersCandyHolderAmount:
                greatersCandyHolderAmount = candies[i]
        
        # the boolean array "result"
        result = [True] * len(candies) # space complexity is O(n) where is the length of candies

        for i in range(len(candies)): # time complexity = O(n)
            if candies[i] + extraCandies >= greatersCandyHolderAmount:
                result[i] = True
            else:
                result[i] = False

        
        return result
        