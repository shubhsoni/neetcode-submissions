class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ans = []
        
        n = len(nums)

        if n == 0:
            return [[lower,upper]]

        #1st interval
        if nums[0] > lower:
            ans.append([
                lower, nums[0]-1
            ])

        #mid intervals
        for i in range(n):
            if nums[i] - nums[i-1] <= 1: #duplicate of diff of 1
                continue
            ans.append([
                nums[i-1] + 1,
                nums[ i ] - 1
            ])

        #last interval
        if nums[-1] < upper:
            ans.append([
                nums[-1] + 1, upper
            ])

        return ans