class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # optimum two pointer

        def cal_water(i,j):
            return (j - i) * (min(heights[i], heights[j]))


        # while l < r
        # left and right pointer
        # check min height of l and r
        # calculate water and take max againts seen so far
        # move pointer with min height 

        l = 0
        r = len(heights)-1
        ans = 0

        while l < r:
            water = cal_water(l,r)
            ans = max(ans, water)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return ans
        
        