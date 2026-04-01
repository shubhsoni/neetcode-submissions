class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0

        l, r = 0, 0
        while l < len(s):

            counter = 0
            sset = set()
            while r<len(s) and s[r] not in sset:
                sset.add(s[r])
                counter += 1
                r += 1
            
            #move l to r
            l += 1
            r = l
            ans = max(ans, counter)

        return ans
