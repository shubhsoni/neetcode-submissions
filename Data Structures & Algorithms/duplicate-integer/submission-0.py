class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_set = set()
        for element in nums:
            if element in unique_set:
                return True
            else:
                unique_set.add(element)
        return False