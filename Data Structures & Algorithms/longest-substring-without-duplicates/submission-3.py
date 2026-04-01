class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # two pointer
        # use set to track duplicate char
        # move r pointer unless dup found. if found rest l and r and repeat untill l<len(s)
        ##this is actualy O(n*m)
        # ans = 0

        # l, r = 0, 0
        # while l < len(s):

        #     counter = 0
        #     sset = set()
        #     while r<len(s) and s[r] not in sset:
        #         sset.add(s[r])
        #         counter += 1
        #         r += 1
            
        #     #move l to r
        #     l += 1
        #     r = l
        #     ans = max(ans, counter)

        # return ans

        ## better approach is sliding window - O(n)
        # shrink window from left
        ans = 0
        sset = set()

        l=0
        r=0
        while l < len(s) and r < len(s):
            while r< len(s) and s[r] in sset:
                sset.remove(s[l])
                l += 1
 
            
            ans = max(ans, r-l+1)
            sset.add(s[r])
            r += 1

        return ans

            


