class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # explore all possible combination -> O(n2)
        # edge cases there can be 0 so division method needs to handle
        # division by zero

        #better
        # two pointer - left running prod and right running prod
        # O(n)
        lprod = nums.copy()
        for i in range(len(nums)):
            if i==0:
                p = 1
                lprod[i] = p
                continue
            p = p * nums[i-1]
            lprod[i] = p

        # i=0, p=1 -> [1]
        # i=1, p = p*1 = 1*1 -> [1,1]
        # i=2, p = 1*nums[2-1] = 1*2 -> [1,1,2]
        # i=3, p = 2*nums[3-1] = 2*4 -> [1,1,2,8]
        
        # n=[ 1, 2, 4, 6]
        # l=[ 1, 1, 2, 8]
        # r=[48,24, 6, 1]
        # a=[48,24,12, 8]

        rprod = nums.copy()
        for i in range(len(nums)-1, -1, -1):
            if i==len(nums)-1:
                p = 1
                rprod[i] = p
                continue
            p = p * nums[i+1]
            rprod[i] = p
        
        # print(lprod, rprod)
        ans = []
        for l,r in zip(lprod,rprod):
            ans.append(l*r) 

        return ans




        