class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # ss = set(nums)
        # return target in ss

        l,r = 0, len(nums)-1

        while l<=r:
            m = l + (r-l)//2

            if nums[m] == target:
                return True

            #left is sorted
            if nums[l] < nums[m]:
                # if num in left
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            # right is sorted
            elif nums[l] > nums[m]:
                # target in right
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

            else:
                l += 1

        return False