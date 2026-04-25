class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        ss = set(nums)
        return target in ss
        