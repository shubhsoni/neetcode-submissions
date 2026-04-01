class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ## brute force - search entire space
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        ## trade of memory with speed
        num_seen_set = set() ## use set for hashset and {} for key-value pair
        for num in nums:
            if num in num_seen_set:
                return True
            else:
                num_seen_set.add(num) # use add method in set for inplace update

        return False 
         