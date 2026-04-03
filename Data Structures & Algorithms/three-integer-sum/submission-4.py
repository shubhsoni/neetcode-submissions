class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # always remember which existing algorithms can be used
        # given a arr input -> SORT

        # SOLVE TWO-SUM-2 problem which has two-pointer approach

        # sort -> for each candidate find other 2 nums with 2 pointer approach
        # key insights 
        #    - if all negative or all positive num left then stop
        #.   - keep shifting pointers right or left for desired conditions

        nums.sort()
        ans = []
        if all(n<0 for n in nums) or all(n>0 for n in nums):
            return []

        for i in range(len(nums)):
            target = - nums[i] 
            # n1 + n2 + n3 = 0 --> n1 + n2 = -n3 (target)

            #search in remaining str
            l = i + 1
            r = len(nums)-1
            while l < r:
                if nums[l] + nums[r] == target:
                    triplet = sorted([nums[i],nums[l],nums[r]])
                    ans.append(tuple(triplet))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return [list(t) for t in set(ans)]