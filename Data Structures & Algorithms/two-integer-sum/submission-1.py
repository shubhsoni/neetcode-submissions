class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force explore all combination 
        # nested for -> O(n^2) complexity

        #optimize - use dict

        #clarify 
        #- are there multiple answers?
        #- fit in memory?
        #- negative/float values?

        #optimized
        complement = {}
        for i in range(len(nums)):
            if nums[i] in complement:
                return [complement[nums[i]], i]
            else:
                complement[target-nums[i]] = i
        return -1
